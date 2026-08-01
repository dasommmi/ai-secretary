from dataclasses import dataclass


@dataclass
class ValidationResult:

    success: bool

    errors: list[str]
