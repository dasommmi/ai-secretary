from pathlib import Path


class StyleLoader:

    @staticmethod
    def load(name: str = "sandy") -> str:

        path = (
                Path(__file__)
                .parent.parent
                / "styles"
                / f"{name}.md"
        )

        return path.read_text(
            encoding="utf-8"
        )