from infrastructure.ai.openrouter import ask_openrouter


class ContentGenerator:

    def generate(self, prompt: str) -> str:

        return ask_openrouter(prompt)
