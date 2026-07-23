from dashpaan.elements.base import Element


class StickyTarget(Element):
    kind = "sticky-target"

    size = "1x1"
    color = "red"
    name = "Dashpaan"
    value = 8
    note = ""
    data = None
    more = None

    def json(self):
        return {
            **super(StickyTarget, self).json(),
            "size": self.size,
            "color": self.color,
            "name": self.name,
            "value": self.value,
            "note": self.note,
            "data": self.data.json() if type(self.data) is StickyTarget.Tab else self.data,  # @todo check for bugs
            "more": self.more.json() if self.more else None
        }

    @classmethod
    def from_json(cls, obj):
        return StickyTarget(**obj)

    class Tab(Element):
        kind = "sticky-target-tab"

        name = "Dashpaan"
        value = 8
        note = ""

        def json(self):
            return {
                **super(StickyTarget.Tab, self).json(),
                "name": self.name,
                "value": self.value,
                "note": self.note,
            }

        @classmethod
        def from_json(cls, obj):
            return StickyTarget.Tab(**obj)

    class More(Element):
        kind = "sticky-target-more"

        icon = "plus"
        action = None

        def json(self):
            return {
                **super(StickyTarget.More, self).json(),
                "icon": self.icon,
                "action": self.action.json() if self.action else None,
            }

        @classmethod
        def from_json(cls, obj):
            return StickyTarget.More(**obj)
