from dashpaan.elements.base import Element


class Flex(Element):
    kind = "flex"

    mode = "vertical"
    breakable = False
    size = "1*1"
    elements = []

    def json(self):
        return {
            **super(Flex, self).json(),
            "mode": self.mode,
            "breakable": self.breakable,
            "size": self.size,
            "elements": [element.json() for element in self.elements]
        }

    @classmethod
    def from_json(cls, obj):
        return Flex(**obj)
