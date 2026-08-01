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
상호명:
{self.store_name}

위치:
{self.location}

방문일:
{self.visit_date}

동행:
{self.companion}

방문시간:
{self.visit_time}

웨이팅:
{self.waiting}

메뉴:
{self.menu}

가격:
{self.price}

음식 후기:
{self.food}

분위기:
{self.atmosphere}

서비스:
{self.service}

좋았던 점:
{self.good}

아쉬운 점:
{self.bad}

재방문:
{self.revisit}

추천 대상:
{self.recommend}

사진 메모:
{self.photo_note}
"""