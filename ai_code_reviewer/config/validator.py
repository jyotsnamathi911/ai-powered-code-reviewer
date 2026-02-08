VALID_SEVERITIES = {"info", "warning", "critical"}


def validate_severity(severity: str) -> None:
    if severity not in VALID_SEVERITIES:
        raise ValueError(
            f"Invalid severity_threshold '{severity}'. "
            f"Must be one of {VALID_SEVERITIES}"
        )


def validate_positive_int(value: int, field_name: str) -> None:
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"{field_name} must be a positive integer")
