from dashpaan.actions.base import Action


class Navigate(Action):
    type = "navigate"

    headers = {}
    payload = {}
    uri = ""
    url = ""

    def json(self):
        return {
            **super(Navigate, self).json(),
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
