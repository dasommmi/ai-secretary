from content.validator.base import BaseValidator
from content.validator.result import ValidationResult


class ContentValidator(BaseValidator):


    def __init__(
            self,
            profile
    ):

        self.profile = profile



    def validate(
            self,
            content: str
    ) -> ValidationResult:


        errors = []


        # 금지 표현 검사

        for word in self.profile["forbidden"]:

            if word in content:

                errors.append(
                    f"금지 표현 발견: {word}"
                )


        # 총평 존재 확인

        if "총평" not in content:

            errors.append(
                "총평 섹션 없음"
            )


        # 제목 길이 검사

        title = content.split("\n")[0]

        max_length = (
            self.profile["title"]
            ["max_length"]
        )


        if len(title) > max_length:

            errors.append(
                "제목 길이 초과"
            )


        if len(content) < 2000:

            errors.append(
                "글자 수 부족: 2000자 미만"
            )


        return ValidationResult(
            success=len(errors) == 0,
            errors=errors
        )