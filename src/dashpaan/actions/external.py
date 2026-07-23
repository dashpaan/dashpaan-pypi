from dashpaan.actions.base import Action


class External(Action):
    type = "external"

    url = ""

    def json(self):
        return {
            **super(External, self).json(),
            "api": {
                "url": self.url,
            }
        }

    @classmethod
    def from_json(cls, obj):
        return External(**obj)
