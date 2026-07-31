from content.template_registry import TemplateRegistry
from content.parser.parser_registry import ParserRegistry
from content.builders.prompt_builder import PromptBuilder
from content.generator.content_generator import ContentGenerator

class ContentService:


    def get_form(
            self,
            content_type: str
    ) -> str:

        template = TemplateRegistry.get_template(
            content_type
        )

        return template.generate_form()



    def parse(
            self,
            content_type: str,
            text: str
    ):

        parser = ParserRegistry.get_parser(
            content_type
        )

        return parser.parse(text)


    def build_prompt(
            self,
            content_type: str,
            request
    ):

        builder = PromptBuilder()

        return builder.build(
            content_type,
            request
        )

    def generate(
            self,
            prompt: str
    ):

        generator = ContentGenerator()

        return generator.generate(prompt)