def format_text(text: str) -> str:
    """Normalize spacing and case while preserving quoted values."""
    text = remove_extra_spaces(text)
    text = lower_case(text)
    return text


def lower_case(text: str) -> str:
    """Convert text to lowercase, preserving quoted string content."""
    parts = text.split("'")

    for i in range(0, len(parts), 2):
        parts[i] = parts[i].lower()

    return "'".join(parts)


def remove_extra_spaces(text: str) -> str:
    """Collapse repeated whitespace into single spaces."""
    return " ".join(text.split())
