from content.templates.base import BaseTemplate


class RestaurantTemplate(BaseTemplate):

    def generate_form(self) -> str:
        return """
🍽 음식점 리뷰 작성

아래 양식을 작성해서 다시 보내주세요.

----------------------------

[기본 정보]
가게명 :
지역 :
방문 날짜 :

[방문]
방문 인원 :
웨이팅 여부 (O/X) :
방문 시간 :

[주문]
주문 메뉴 :
가격 :

[후기]
음식 :
분위기 :
서비스 :
좋았던 점 :
아쉬웠던 점 :

[마무리]
재방문 의사 :
추천 대상 :
사진 메모(선택) :

----------------------------
""".strip()
