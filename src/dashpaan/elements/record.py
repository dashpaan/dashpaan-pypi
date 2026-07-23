from dashpaan.elements.base import Element


class Record(Element):
    kind = "record"

    id = None
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
            **super(Record, self).json(),
            "title": self.title,
            "size": self.size,
            "id": self.id,
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
        return Record(**obj)

    class Profile(Element):
        kind = "record-profile"

        name = None
        description = None
        image = None
        action = None

        def json(self):
            return {
                **super(Record.Profile, self).json(),
                "name": self.name,
                "description": self.description,
                "image": self.image,
                "action": self.action.json() if self.action else None,
            }

        @classmethod
        def from_json(cls, obj):
            return Record.Profile(**obj)

    class Badge(Element):
        kind = "record-badge"

        color = None
        icon = None
        action = None

        def json(self):
            return {
                **super(Record.Badge, self).json(),
                "color": self.color,
                "icon": self.icon,
                "action": self.action.json() if self.action else None,
            }

        @classmethod
        def from_json(cls, obj):
            return Record.Badge(**obj)

    class MenuItem(Element):
        kind = "record-menu-item"

        name = None
        action = None

        def json(self):
            return {
                **super(Record.MenuItem, self).json(),
                "name": self.name,
                "action": self.action.json() if self.action else None,
            }

        @classmethod
        def from_json(cls, obj):
            return Record.MenuItem(**obj)
