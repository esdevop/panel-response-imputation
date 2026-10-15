"""Checks for the user-selected blank-as-zero policy, not the historical audit."""

import pytest

from src.experiments.multiselect_contracts import evaluate_synthetic
from src.life_changes import OPTION_TARGETS, SOURCE_QUESTION_ID, encode_life_changes


@pytest.mark.parametrize("raw", ["", " \t\n", None])
def test_blank_becomes_five_eligible_zeros(raw):
    labels = encode_life_changes(raw)
    assert len(labels) == 5
    assert set(labels.values()) == {"0"}
    truth = {("synthetic_participant", target): label for target, label in labels.items()}
    result = evaluate_synthetic(
        truth, truth.copy(), {target: SOURCE_QUESTION_ID for target in labels}
    )
    assert all(row["n_expected"] == row["n_eligible"] == 1 for row in result["metrics_by_target"])
    assert result["summary"]["n_observations"] == 5


def test_selected_options_are_trimmed_and_remaining_options_are_zero():
    labels = encode_life_changes("Lost a job ,Had a child")
    assert labels["Q-life-changes-lost-job"] == "1"
    assert labels["Q-life-changes-had-child"] == "1"
    assert list(labels.values()).count("0") == 3


def test_all_five_options_selected():
    assert set(encode_life_changes(",".join(option for option, _ in OPTION_TARGETS)).values()) == {"1"}


@pytest.mark.parametrize("raw", ["Unknown", "Lost a job,Lost a job", "None of the above", ","])
def test_unexpected_encoding_is_not_silently_treated_as_blank(raw):
    with pytest.raises(ValueError):
        encode_life_changes(raw)
