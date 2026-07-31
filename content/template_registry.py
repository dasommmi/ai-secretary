from content.content_type import ContentType
from content.templates.restaurant import RestaurantTemplate


class TemplateRegistry:

    _templates = {
        ContentType.RESTAURANT: RestaurantTemplate,
    }

    @classmethod
    def get_template(cls, content_type: str):

        try:
            content_type = ContentType(content_type.lower())

        except ValueError:
            raise ValueError(
                f"지원하지 않는 콘텐츠 타입입니다. ({content_type})"
            )

        return cls._templates[content_type]()