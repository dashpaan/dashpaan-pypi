from dashpaan.elements.base import Element


class Block(Element):
    kind = "block"

    mode = "vertical"
    breakable = False
    rounded = False
    background = None
    size = "1*1"
    elements = []

    def json(self):
        return {
            **super(Block, self).json(),
            "mode": self.mode,
            "breakable": self.breakable,
            "size": self.size,
            "rounded": self.rounded,
            "background": self.background,
            "elements": [element.json() for element in self.elements]
        }

    @classmethod
    def from_json(cls, obj):
        return Block(**obj)
