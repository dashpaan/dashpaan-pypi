from src.dashpaan.elements.base import Element


class External(Element):
    kind = "action"
    type = "external"

    url = ""

    def json(self):
        return {
            **super(External, self).json(),
            "kind": self.kind,
            "type": self.type,
            "api": {
                "url": self.url,
            }
        }

    @classmethod
    def from_json(cls, obj):
        return External(**obj)
