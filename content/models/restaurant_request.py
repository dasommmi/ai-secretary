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