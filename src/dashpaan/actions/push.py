from dashpaan.actions.base import Action


class Push(Action):
    type = "push"

    headers = {}
    payload = {}
    url = ""
    data = False

    def json(self):
        return {
            **super(Push, self).json(),
            "data": self.data,
            "api": {
                "payload": self.payload,
                "headers": self.headers,
                "url": self.url
            }
        }

    @classmethod
    def from_json(cls, obj):
        return Push(**obj)
