class Element:
    kind = None
    version = "v1"

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

        if args and hasattr(self, "elements"):
            self.elements = [x for x in args if x]

    def json(self):
        return {
            "kind": self.kind,
            "version": self.version
        }
