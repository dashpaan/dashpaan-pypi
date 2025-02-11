from dashpaan.elements.base import Element


class Prompt(Element):
    kind = "action"
    type = "prompt"

    elements = []
    close = False
    print = False
    title = None

    def json(self):
        return {
            **super(Prompt, self).json(),
            "kind": self.kind,
            "type": self.type,
            "close": self.close,
            "print": self.print,
            "title": self.title,
            "elements": [element.json() for element in self.elements]
        }

    @classmethod
    def from_json(cls, obj):
        return Prompt(**obj)
