from pathlib import Path

from .schema import ReviewerConfig, RuleConfig
from .loader import load_pyproject
from .validator import validate_severity, validate_positive_int


def load_config(pyproject_path: Path | None = None) -> ReviewerConfig:
    raw = load_pyproject(pyproject_path)

    tool_cfg = raw.get("tool", {}).get("ai_code_reviewer", {})
    rules_cfg = tool_cfg.get("rules", {})

    rules = RuleConfig(
        max_function_length=rules_cfg.get("max_function_length", 50),
        max_cyclomatic_complexity=rules_cfg.get("max_cyclomatic_complexity", 10),
        require_type_hints=rules_cfg.get("require_type_hints", True),
    )

    config = ReviewerConfig(
        severity_threshold=tool_cfg.get("severity_threshold", "warning"),
        exclude_paths=tool_cfg.get("exclude_paths", []),
        rules=rules,
    )

    validate_severity(config.severity_threshold)
    validate_positive_int(
        config.rules.max_function_length, "max_function_length"
    )
    validate_positive_int(
        config.rules.max_cyclomatic_complexity,
        "max_cyclomatic_complexity",
    )

    return config
