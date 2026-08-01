from content.content_type import ContentType
from content.parser.restaurant_parser import RestaurantParser


class ParserRegistry:

    _parsers = {
        ContentType.RESTAURANT: RestaurantParser,
    }

    @classmethod
    def get_parser(cls, content_type: str):

        try:
            content_type = ContentType(content_type.lower())

        except ValueError:
            raise ValueError(f"지원하지 않는 콘텐츠 타입입니다. ({content_type})")

        parser = cls._parsers.get(content_type)

        if parser is None:
            raise ValueError(f"아직 준비되지 않은 콘텐츠 타입입니다. ({content_type.value})")

        return parser()
