from dataclasses import dataclass


@dataclass
class RestaurantRequest:

    store_name: str = ""
    location: str = ""
    visit_date: str = ""

    companion: str = ""
    waiting: str = ""
    visit_time: str = ""

    menu: str = ""
    price: str = ""

    food: str = ""
    atmosphere: str = ""
    service: str = ""

    good: str = ""
    bad: str = ""

    revisit: str = ""
    recommend: str = ""
    photo_note: str = ""

    def to_prompt(self):

        return f"""
[기본 정보]

가게명:
{self.store_name}

지역:
{self.location}

방문 날짜:
{self.visit_date}


[방문]

방문 인원:
{self.companion}

웨이팅:
{self.waiting}

방문 시간:
{self.visit_time}


[주문]

메뉴:
{self.menu}

가격:
{self.price}


[후기]

음식:
{self.food}

분위기:
{self.atmosphere}

서비스:
{self.service}

좋았던 점:
{self.good}

아쉬웠던 점:
{self.bad}


[마무리]

재방문 의사:
{self.revisit}

추천 대상:
{self.recommend}

사진 메모:
{self.photo_note}
"""
