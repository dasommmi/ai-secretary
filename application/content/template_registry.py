from application.content.content_type import ContentType
from application.content.templates.restaurant import RestaurantTemplate


class TemplateRegistry:

    _templates = {
        ContentType.RESTAURANT: RestaurantTemplate,
    }

    @classmethod
    def get_template(cls, content_type: str):

        try:
            content_type = ContentType(content_type.lower())

        except ValueError:
            raise ValueError(f"지원하지 않는 콘텐츠 타입입니다. ({content_type})")

        template = cls._templates.get(content_type)

        if template is None:
            raise ValueError(f"아직 준비되지 않은 콘텐츠 타입입니다. ({content_type.value})")

        return template()
