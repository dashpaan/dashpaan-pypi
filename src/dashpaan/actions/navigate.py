from dashpaan.actions.base import Action


class Navigate(Action):
    type = "navigate"

    headers = {}
    payload = {}
    uri = ""
    url = ""
    method = "GET"

    def json(self):
        return {
            **super(Navigate, self).json(),
            "api": {
                "payload": self.payload,
                "headers": self.headers,
                "url": self.url,
                "uri": self.uri,
                "method": self.method
            }
        }

    @classmethod
    def from_json(cls, obj):
        return Navigate(**obj)
