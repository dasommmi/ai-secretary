from abc import ABC, abstractmethod


class BaseTemplate(ABC):

    @abstractmethod
    def generate_form(self) -> str:
        """입력 양식을 반환한다."""
        pass
