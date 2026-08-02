from ai.openrouter import ask_openrouter

from knowledge.prompt.knowledge_prompt import build_knowledge_prompt


class KnowledgeGenerator:

    def generate(self, category: str) -> str:

        prompt = build_knowledge_prompt(category)

        return ask_openrouter(prompt)
