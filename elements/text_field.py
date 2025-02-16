from dashpaan.elements.base import Element


class TextField(Element):
    kind = "text-field"

    name = None
    label = None
    required = False
    default = None
    defaultValue = None

    def json(self):
        return {
            **super(TextField, self).json(),
            "name": self.name,
            "label": self.label,
            "required": self.required,
            "default": self.defaultValue if self.defaultValue else self.default
        }

    @classmethod
    def from_json(cls, obj):
        return TextField(**obj)
