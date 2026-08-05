from application.knowledge.knowledge_generator import KnowledgeGenerator


class KnowledgeService:

    def __init__(self):

        self.generator = KnowledgeGenerator()

    def generate(self, category: str):

        return self.generator.generate(category)
