from content.prompt.restaurant_prompt import (
    build_restaurant_prompt
)


class PromptBuilder:


    def build(
            self,
            content_type: str,
            request
    ) -> str:


        if content_type == "restaurant":

            data = request.__dict__

            return build_restaurant_prompt(data)


        raise ValueError(
            f"지원하지 않는 prompt type입니다. {content_type}"
        )