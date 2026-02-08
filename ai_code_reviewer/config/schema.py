from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class RuleConfig:
    max_function_length: int = 50
    max_cyclomatic_complexity: int = 10
    require_type_hints: bool = True


@dataclass
class ReviewerConfig:
    severity_threshold: str = "warning"
    exclude_paths: List[str] = field(default_factory=list)
    rules: RuleConfig = field(default_factory=RuleConfig)
