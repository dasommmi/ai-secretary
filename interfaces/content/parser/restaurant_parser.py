from interfaces.content.parser.base import BaseParser
from domain.content.restaurant_request import RestaurantRequest


class RestaurantParser(BaseParser):

    FIELD_MAPPING = {
        "가게명": "store_name",
        "지역": "location",
        "방문 날짜": "visit_date",
        "방문 인원": "companion",
        "웨이팅": "waiting",
        "방문 시간": "visit_time",
        "주문 메뉴": "menu",
        "가격": "price",
        "음식": "food",
        "분위기": "atmosphere",
        "서비스": "service",
        "좋았던 점": "good",
        "아쉬웠던 점": "bad",
        "재방문 의사": "revisit",
        "추천 대상": "recommend",
        "사진 메모(선택)": "photo_note",
    }

    def parse(self, text: str) -> RestaurantRequest:

        data = {}

        lines = text.splitlines()

        for line in lines:

            if ":" not in line:
                continue

            key, value = line.split(":", 1)

            key = key.strip()
            value = value.strip()

            if key in self.FIELD_MAPPING:
                field = self.FIELD_MAPPING[key]
                data[field] = value

        return RestaurantRequest(**data)
