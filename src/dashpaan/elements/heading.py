from dashpaan.elements.base import Element


class Heading(Element):
    kind = "heading"

    title = ""
    subtitle = ""
    align = "center"

    def json(self):
        return {
            **super(Heading, self).json(),
            "title": self.title,
            "subtitle": self.subtitle,
            "align": self.align
        }

    @classmethod
    def from_json(cls, obj):
        return Heading(**obj)
