from content.builders.profile_loader import (
    ProfileLoader
)

from content.template_registry import (
    TemplateRegistry
)



class PromptBuilder:


    def build(
            self,
            content_type: str,
            request
    ) -> str:


        template = (
            TemplateRegistry
            .get(content_type)
        )


        profile = (
            ProfileLoader
            .load("sandy")
        )


        return f"""
# Content Template

{template}


# Writing Profile

Name:
{profile["name"]}


## Title Rules

{profile["title"]}


## Tone

{profile["tone"]}


## Writing Flow

{profile["flow"]}


## Preferred Expressions

{profile["preferred"]}


## Forbidden Expressions

{profile["forbidden"]}


## User Content

{request.to_prompt()}

"""