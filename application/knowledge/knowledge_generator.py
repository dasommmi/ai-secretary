from infrastructure.ai.openrouter import ask_openrouter

from infrastructure.ai.prompts.knowledge_prompt import build_knowledge_prompt


class KnowledgeGenerator:

    def generate(self, category: str) -> str:

        prompt = build_knowledge_prompt(category)

        return ask_openrouter(prompt)
