from dataclasses import dataclass


@dataclass
class CategoryProfile:

    category: str

    description: str

    prompt_rule: str
