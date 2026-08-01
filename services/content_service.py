from content.template_registry import TemplateRegistry
from content.parser.parser_registry import ParserRegistry
from content.builders.prompt_builder import PromptBuilder
from content.generator.content_generator import ContentGenerator
from content.writer.markdown_writer import MarkdownWriter

from content.builders.profile_loader import ProfileLoader
from content.validator.content_validator import ContentValidator


class ContentService:

    def __init__(self):

        self.generator = ContentGenerator()

        self.writer = MarkdownWriter()

        profile = ProfileLoader.load("sandy")

        self.validator = ContentValidator(profile)

    def get_form(self, content_type: str) -> str:

        template = TemplateRegistry.get_template(content_type)

        return template.generate_form()

    def parse(self, content_type: str, text: str):

        parser = ParserRegistry.get_parser(content_type)

        return parser.parse(text)

    def build_prompt(self, content_type: str, request):

        builder = PromptBuilder()

        return builder.build(content_type, request)

    def generate(self, prompt: str):

        retry = 0

        while retry < 3:

            content = self.generator.generate(prompt)

            result = self.validator.validate(content)

            if result.success:

                return content

            prompt += f"""

다음 문제를 수정해서 다시 작성해주세요.

문제:
{result.errors}

"""

            retry += 1

        return content

    def write_markdown(self, content_type: str, content: str):

        return self.writer.write(content_type, content)
