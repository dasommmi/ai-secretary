from content.builders.profile_loader import (
    ProfileLoader
)


class PromptBuilder:


    def build(
            self,
            content_type: str,
            request
    ) -> str:


        profile = (
            ProfileLoader
            .load("sandy")
        )


        return f"""
# Role

당신은 네이버 블로그 전문 에디터입니다.


# Content Type

{content_type}


# Writing Profile

## Name

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


# Writing Requirement

아래 정보를 기반으로 실제 방문자가 작성한 것처럼 자연스러운 네이버 블로그 글을 작성하세요.

반드시 아래 조건을 지켜주세요.

## 분량

- 전체 글자 수는 공백 포함 최소 2,000자 이상 작성
- 방문 과정, 음식 후기, 공간 후기, 총평을 충분히 상세하게 작성
- 짧은 요약문 형태로 작성하지 말 것


## 글 스타일

- 실제 방문자가 작성한 후기처럼 자연스럽게 작성
- 과장 표현 금지
- 광고처럼 보이는 표현 금지
- 직접 경험한 느낌 유지
- 장점과 아쉬운 점 모두 작성
- 개인적인 의견 포함


## 문단 구성

- 한 문단은 2~4줄 정도로 작성
- 모바일에서 읽기 편하도록 작성
- 주요 내용 앞에는 소제목 사용


## 반드시 포함

- 방문 계기
- 위치 및 기본 정보
- 방문 당시 상황
- 매장 분위기
- 주문 메뉴 설명
- 음식 맛 평가
- 좋았던 점
- 아쉬웠던 점
- 총평
- 재방문 의사


# User Information

{request.to_prompt()}

"""