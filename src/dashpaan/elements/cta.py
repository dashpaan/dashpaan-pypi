from dashpaan.elements.base import Element
from dashpaan.actions.prompt import Prompt


class CTA(Element):
    kind = "cta"

    size = "1*1.5"
    title = None
    icon = None
    action = None
    color = "black"
    background = "transparent"
    border = False

    def json(self):
        return {
            **super(CTA, self).json(),
            "size": self.size,
            "title": self.title,
            "icon": self.icon,
            "action": self.action.json() if self.action else None,
            "color": self.color,
            "background": self.background,
            "border": self.border
        }

    @classmethod
    def from_json(cls, obj):
        return CTA(**obj)
