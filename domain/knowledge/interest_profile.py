from dataclasses import dataclass, field


@dataclass
class InterestProfile:

    interests: list[str] = field(default_factory=list)

    def add_interest(self, interest: str):

        if interest not in self.interests:
            self.interests.append(interest)

    def remove_interest(self, interest: str):

        if interest in self.interests:
            self.interests.remove(interest)
