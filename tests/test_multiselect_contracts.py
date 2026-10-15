"""Deterministic checks on synthetic inputs only."""

import pytest

from src.experiments.multiselect_contracts import (
    encode_selection,
    evaluate_synthetic,
    normalize_pdf_text,
    synthetic_example,
)


def test_pdf_search_normalizes_word_linebreaks():
    text = normalize_pdf_text("life\nchanges?\nNone\nof\nthe\nabove")
    assert "life changes" in text
    assert "None of the above" in text


def test_blank_is_unknown():
    assert encode_selection(" ", ["A", "B"]) == [None, None]


def test_selection_trims_whitespace():
    assert encode_selection("A , B", ["A", "B", "C"]) == [1, 1, 0]


@pytest.mark.parametrize("raw", ["unknown", "A,A"])
def test_invalid_selection_rejected(raw):
    with pytest.raises(ValueError):
        encode_selection(raw, ["A", "B"])


def test_hand_calculated_synthetic_metrics():
    result = synthetic_example()
    assert [row["value"] for row in result["metrics_by_target"]] == [1.0, 1.0, 0.0]
    assert [row["n_eligible"] for row in result["metrics_by_target"]] == [1, 2, 2]
    assert all(row["n_expected"] == 2 for row in result["metrics_by_target"])
    assert result["summary"]["target_macro"] == pytest.approx(2 / 3)
    assert result["summary"]["question_macro"] == 0.5
    assert result["summary"]["n_observations"] == 5


@pytest.mark.parametrize("predictions", [{}, {("p", "a"): "0", ("extra", "a"): "1"}])
def test_coverage_mismatch_rejected(predictions):
    with pytest.raises(ValueError, match="coverage"):
        evaluate_synthetic({("p", "a"): "1"}, predictions, {"a": "question"})


def test_invalid_prediction_rejected():
    with pytest.raises(ValueError, match="Invalid"):
        evaluate_synthetic({("p", "a"): "1"}, {("p", "a"): "invalid"}, {"a": "question"})


def test_no_eligible_truth_is_undefined():
    result = evaluate_synthetic({("p", "a"): None}, {("p", "a"): "1"}, {"a": "question"})
    assert result["metrics_by_target"][0]["status"] == "undefined"
    assert result["summary"] is None


def test_alignment_uses_keys_not_order():
    truth = {("p1", "a"): "1", ("p2", "a"): "0"}
    predictions = {("p2", "a"): "0", ("p1", "a"): "1"}
    assert evaluate_synthetic(truth, predictions, {"a": "q"})["summary"]["target_macro"] == 1
