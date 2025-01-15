from dashpaan.elements.base import Element


class Select(Element):
    kind = "select"

    name = ""
    default = ""
    multiple = False
    label = ""
    options = []

    def json(self):
        return {
            **super(Select, self).json(),
            "name": self.name,
            "default": self.default,
            "multiple": self.multiple,
            "label": self.label,
            "options": self.options
        }

    @classmethod
    def from_json(cls, obj):
        return Select(**obj)

