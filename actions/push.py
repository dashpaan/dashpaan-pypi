from dashpaan.elements.base import Element


class Push(Element):
    kind = "action"
    type = "push"

    headers = {}
    payload = {}
    url = ""

    def json(self):
        return {
            **super(Push, self).json(),
            "kind": self.kind,
            "type": self.type,
            "api": {
                "payload": self.payload,
                "headers": self.headers,
                "url": self.url
            }
        }

    @classmethod
    def from_json(cls, obj):
        return Push(**obj)
