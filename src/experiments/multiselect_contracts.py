"""Audit frozen survey encoding; exercise contracts on explicitly synthetic data."""

import argparse
import csv
import hashlib
import io
import json
import platform
import subprocess
import time
import zipfile
from collections import Counter
from datetime import datetime, timezone
from importlib.metadata import version
from pathlib import Path

from pypdf import PdfReader


QUESTION = "Q-life-changes"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def encode_selection(raw: str, options: list[str]) -> list[int | None]:
    """Conservatively preserve blank as unknown, not evidence of no selection."""
    if not raw.strip():
        return [None] * len(options)
    selected = [part.strip() for part in raw.split(",")]
    if len(set(selected)) != len(selected) or not set(selected) <= set(options):
        raise ValueError("Unknown or duplicate option")
    return [int(option in selected) for option in options]


def evaluate_synthetic(truth: dict, predictions: dict, source_questions: dict) -> dict:
    """Tiny contract prototype, not the project's general evaluator."""
    if predictions.keys() != truth.keys():
        raise ValueError("Prediction coverage differs from expected pairs")
    if any(value not in ("0", "1") for value in predictions.values()):
        raise ValueError("Invalid binary prediction")
    rows = []
    for target in sorted(source_questions):
        expected = [key for key in truth if key[1] == target]
        eligible = [key for key in expected if truth[key] is not None]
        value = (
            sum(predictions[key] == truth[key] for key in eligible) / len(eligible)
            if eligible else None
        )
        rows.append({
            "target_id": target, "metric_id": "accuracy",
            "value": value, "n_expected": len(expected),
            "n_eligible": len(eligible),
            "status": "ok" if eligible else "undefined",
            "reason": None if eligible else "no eligible ground truth",
        })
    # Undefined aggregates are intentionally not silently computed over fewer targets.
    if any(row["value"] is None for row in rows):
        return {"metrics_by_target": rows, "summary": None}
    groups = {}
    for row in rows:
        groups.setdefault(source_questions[row["target_id"]], []).append(row["value"])
    return {
        "metrics_by_target": rows,
        "summary": {
            "target_macro": sum(row["value"] for row in rows) / len(rows),
            "question_macro": sum(sum(v) / len(v) for v in groups.values()) / len(groups),
            "n_observations": sum(row["n_eligible"] for row in rows),
            "n_targets": len(rows),
        },
    }


def synthetic_example() -> dict:
    truth = {
        ("synthetic_1", "a"): "1", ("synthetic_2", "a"): None,
        ("synthetic_1", "b"): "0", ("synthetic_2", "b"): "1",
        ("synthetic_1", "c"): "1", ("synthetic_2", "c"): "0",
    }
    predictions = {key: "0" for key in truth}
    predictions[("synthetic_1", "a")] = "1"
    predictions[("synthetic_2", "b")] = "1"
    predictions[("synthetic_2", "c")] = "1"
    return evaluate_synthetic(truth, predictions, {"a": "multi", "b": "multi", "c": "single"})


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, default=Path("data/raw/archive/dataverse_files.zip"))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    with zipfile.ZipFile(args.archive) as archive:
        survey_bytes = archive.read("survey.csv")
        fields_bytes = archive.read("fields.csv")
        pdf_bytes = archive.read("survey-instrument.pdf")
    rows = list(csv.DictReader(io.StringIO(survey_bytes.decode("utf-8-sig"))))
    raw_values = [row[QUESTION] for row in rows]
    options = sorted({part.strip() for value in raw_values if value.strip() for part in value.split(",")})
    encoded = [encode_selection(value, options) for value in raw_values]
    fields = list(csv.reader(io.StringIO(fields_bytes.decode("utf-8-sig"))))
    multi_questions = [row for row in fields[1:] if any(term in row[1].lower() for term in ("all that apply", "one or more"))]
    pdf_pages = [page.extract_text() for page in PdfReader(io.BytesIO(pdf_bytes)).pages]
    local_pdf_text = Path("data/raw/survey-instrument-extracted.txt")
    local_pdf_text.write_text("\n\n".join(f"PAGE {i + 1}\n{text}" for i, text in enumerate(pdf_pages)))
    result = {
        "question": "Can blank life-change selections be distinguished from no selected options?",
        "prior": "Explicit coding or instrument evidence may distinguish missing from none; otherwise inconclusive.",
        "git_sha": sha,
        "read_at_utc": datetime.now(timezone.utc).isoformat(),
        "archive_sha256": digest(args.archive.read_bytes()),
        "member_sha256": {"survey.csv": digest(survey_bytes), "fields.csv": digest(fields_bytes), "survey-instrument.pdf": digest(pdf_bytes)},
        "uv_lock_sha256": digest(Path("uv.lock").read_bytes()),
        "python": platform.python_version(), "platform": platform.platform(),
        "packages": {name: version(name) for name in ("polars", "pytest", "pypdf")},
        "n_rows": len(rows),
        "blank_by_column": {col: sum(not row[col].strip() for row in rows) for col in rows[0]},
        "refusal_by_column": {col: sum("prefer not to say" in row[col].lower() for row in rows) for col in rows[0]},
        "multi_select_questions_from_wording": multi_questions,
        "life_changes": {
            "n_blank": sum(not value.strip() for value in raw_values),
            "n_distinct_nonblank_combinations": len({value for value in raw_values if value.strip()}),
            "options": options,
            "whitespace_affected_rows": sum(any(part != part.strip() for part in value.split(",")) for value in raw_values if value.strip()),
            "binary_counts_conservative": {option: {str(key): count for key, count in Counter(row[i] for row in encoded).items()} for i, option in enumerate(options)},
            "roundtrip_nonblank_ok": all({part.strip() for part in raw.split(",")} == {option for option, flag in zip(options, flags) if flag == 1} for raw, flags in zip(raw_values, encoded) if raw.strip()),
        },
        "instrument_pages_to_review": [i + 1 for i, text in enumerate(pdf_pages) if "life changes" in text.lower()],
        "synthetic_only": synthetic_example(),
        "scope": "Encoding audit of full survey, no model training, split selection or test performance evaluation. Synthetic metrics are not dataset performance.",
    }
    result["duration_seconds"] = time.perf_counter() - started
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Aggregate results: {args.output}; instrument text (untracked): {local_pdf_text}")


if __name__ == "__main__":
    main()
