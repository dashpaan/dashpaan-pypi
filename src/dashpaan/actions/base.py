class Action:
    kind = "action"
    version = "v1"
    type = ""

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

        if args and hasattr(self, "elements"):
            self.elements = args

    def json(self):
        return {
            "kind": self.kind,
            "version": self.version,
            "type": self.type,
        }
