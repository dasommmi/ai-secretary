from content.builders.style_loader import StyleLoader
from content.template_registry import TemplateRegistry


class PromptBuilder:

    def build(
            self,
            content_type: str,
            request,
    ) -> str:

        template = TemplateRegistry.get(content_type)

        style = StyleLoader.load()

        return f"""
# Template

{template}

----------------------------------------

# Style

{style}

----------------------------------------

# User Input

{request.to_prompt()}
"""