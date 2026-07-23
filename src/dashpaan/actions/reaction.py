from dashpaan.actions.base import Action


class Reaction:
    action = Action()

    def __init__(self, action):
        self.action = action

    def json(self):
        return {
            "reaction": self.action.json(),
        }

    @classmethod
    def from_json(cls, obj):
        return Reaction(**obj)
