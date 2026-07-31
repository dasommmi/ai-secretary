from content.template_manager import TemplateManager


class ContentService:

    def get_form(self, content_type: str) -> str:

        template = TemplateManager.get_template(content_type)

        return template.generate_form()