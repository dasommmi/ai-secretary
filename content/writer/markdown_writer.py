from datetime import datetime
from pathlib import Path


class MarkdownWriter:

    BASE_PATH = Path("generated")

    def write(self, content_type: str, content: str) -> str:

        folder = self.BASE_PATH / content_type

        folder.mkdir(parents=True, exist_ok=True)

        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".md"

        file_path = folder / filename

        file_path.write_text(content, encoding="utf-8")

        return str(file_path)
