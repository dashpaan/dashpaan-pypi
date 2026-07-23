from dashpaan.actions.base import Action


class Reaction:
    kind = "action"
    version = "v1"

    action = Action()

    def __init__(self, action):
        self.action = action

    def json(self):
        return {
            "kind": self.kind,
            "version": self.version,
            "reaction": self.action.json(),
        }

    @classmethod
    def from_json(cls, obj):
        return Reaction(**obj)
