from content.template_registry import TemplateRegistry
from content.parser.parser_registry import ParserRegistry


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