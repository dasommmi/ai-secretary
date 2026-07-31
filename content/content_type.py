from enum import Enum


class ContentType(str, Enum):

    RESTAURANT = "restaurant"
    CAFE = "cafe"
    TRAVEL = "travel"
    DEVELOPMENT = "development"