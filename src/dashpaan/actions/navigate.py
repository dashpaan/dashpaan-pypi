from src.dashpaan.elements.base import Element


class Navigate(Element):
    kind = "action"
    type = "navigate"

    headers = {}
    payload = {}
    uri = ""
    url = ""

    def json(self):
        return {
            **super(Navigate, self).json(),
            "kind": self.kind,
            "type": self.type,
            "api": {
                "payload": self.payload,
                "headers": self.headers,
                "url": self.url,
                "uri": self.uri
            }
        }

    @classmethod
    def from_json(cls, obj):
        return Navigate(**obj)
