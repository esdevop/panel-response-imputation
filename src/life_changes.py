"""Fixed encoding policy for the frozen survey's life-change question."""

SOURCE_QUESTION_ID = "Q-life-changes"
OPTION_TARGETS = (
    ("Lost a job", "Q-life-changes-lost-job"),
    ("Divorce", "Q-life-changes-divorce"),
    ("Moved place of residence", "Q-life-changes-moved"),
    ("Became pregnant", "Q-life-changes-pregnant"),
    ("Had a child", "Q-life-changes-had-child"),
)


def encode_life_changes(raw: str | None) -> dict[str, str]:
    """Return five eligible binary labels; a blank CSV cell means all zeros.

    This is the user-selected published-response policy, not a claim about
    original response collection. None represents a blank cell parsed as null.
    Unknown options still fail rather than silently becoming negative labels.
    """
    selected = [] if raw is None or not raw.strip() else [part.strip() for part in raw.split(",")]
    allowed = {option for option, _ in OPTION_TARGETS}
    if len(selected) != len(set(selected)) or not set(selected) <= allowed:
        raise ValueError("Unknown or duplicate life-change option")
    return {target: "1" if option in selected else "0" for option, target in OPTION_TARGETS}
