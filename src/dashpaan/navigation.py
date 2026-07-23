import uuid

from dashpaan.elements.base import Element


class Navigation(Element):
    kind = "navigation"

    elements = []

    def json(self):
        return {
            **super(Navigation, self).json(),
            "items": self.elements
        }

    @classmethod
    def from_json(cls, obj):
        return Navigation(**obj)

    class Item(Element):
        kind = "nav-item"

        id = uuid.uuid4().hex
        title = ""
        icon = None
        action = None

        def json(self):
            return {
                **super(Navigation.Item, self).json(),
                "id": self.id,
                "title": self.title,
                "type": "item",
                "icon": self.icon,
                "action": self.action.json() if self.action else None
            }

        @classmethod
        def from_json(cls, obj):
            return Navigation.Item(**obj)

    class Group(Element):
        kind = "nav-group"

        id = uuid.uuid4().hex
        title = ""
        icon = None
        elements = []

        def json(self):
            return {
                **super(Navigation.Group, self).json(),
                "id": self.id,
                "title": self.title,
                "type": "group",
                "icon": self.icon,
                "items": self.elements
            }

        @classmethod
        def from_json(cls, obj):
            return Navigation.Group(**obj)
