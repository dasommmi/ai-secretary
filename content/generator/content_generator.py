from ai.openrouter import ask


class ContentGenerator:


    def generate(
            self,
            prompt: str
    ) -> str:

        return ask(prompt)