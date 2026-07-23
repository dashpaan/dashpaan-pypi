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
            "cover": self.cover,
            "icons": self.icons,
            "badges": [x.json() for x in self.badges] if self.badges else None,
            "boxes": self.boxes,
            "menu": [x.json() for x in self.menu] if self.menu else None,
            "people": [x.json() for x in self.people] if self.people else None,
            "profile": self.profile.json() if self.profile else None,
            "description": self.description,
            "cover": self.cover,
            "action": self.action.json() if self.action else None,
        }

    @classmethod
    def from_json(cls, obj):
        return Card(**obj)

    class Profile(Element):
        kind = "card-profile"

        name = None
        description = None
        image = None
        action = None

        def json(self):
            return {
                **super(Card.Profile, self).json(),
                "name": self.name,
                "description": self.description,
                "image": self.image,
                "action": self.action.json() if self.action else None,
            }

        @classmethod
        def from_json(cls, obj):
            return Card.Profile(**obj)

    class Badge(Element):
        kind = "card-badge"

        color = None
        icon = None
        title = None
        action = None

        def json(self):
            return {
                **super(Card.Badge, self).json(),
                "color": self.color,
                "icon": self.icon,
                "title": self.title,
                "action": self.action.json() if self.action else None,
            }

        @classmethod
        def from_json(cls, obj):
            return Card.Badge(**obj)

    class MenuItem(Element):
        kind = "card-menu-item"

        name = None
        action = None

        def json(self):
            return {
                **super(Card.MenuItem, self).json(),
                "name": self.name,
                "action": self.action.json() if self.action else None,
            }

        @classmethod
        def from_json(cls, obj):
            return Record.MenuItem(**obj)
