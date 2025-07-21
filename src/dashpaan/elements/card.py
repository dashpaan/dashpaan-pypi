from src.dashpaan.elements.base import Element


class Card(Element):
    kind = "card"

    icons = None
    cover = None
    size = None
    title = None
    boxes = None
    menu = None
    description = None

    def json(self):
        return {
            **super(Card, self).json(),
            "title": self.title,
            "size": self.size,
            "icons": self.icons,
            "boxes": self.boxes,
            "menu": self.menu,
            "description": self.description,
            "cover": self.cover
        }

    @classmethod
    def from_json(cls, obj):
        return Card(**obj)
