from dashpaan.elements.base import Element


class Card(Element):
    kind = "card"

    icons = None
    badges = None
    cover = None
    size = None
    title = None
    boxes = None
    menu = None
    people = None
    profile = None
    description = None
    action = None

    def json(self):
        return {
            **super(Card, self).json(),
            "title": self.title,
            "size": self.size,
            "icons": self.icons,
            "badges": self.badges,
            "boxes": self.boxes,
            "menu": self.menu,
            "people": self.people,
            "profile": self.profile,
            "description": self.description,
            "cover": self.cover,
            "action": self.action.json() if self.action else None,
        }

    @classmethod
    def from_json(cls, obj):
        return Card(**obj)
