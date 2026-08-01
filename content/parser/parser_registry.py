from content.content_type import ContentType
from content.parser.restaurant_parser import RestaurantParser


class ParserRegistry:

    _parsers = {
        ContentType.RESTAURANT: RestaurantParser,
    }

    @classmethod
    def get_parser(cls, content_type: str):

        content_type = ContentType(content_type.lower())

        parser = cls._parsers.get(content_type)

        if parser is None:
            raise ValueError(f"지원하지 않는 parser입니다. {content_type}")

        return parser()
