from src.dashpaan.elements.base import Element


class FormElementUploadImage(Element):
    kind = "formElementUploadImage"

    name = ""
    label = ""
    default = ""

    def json(self):
        return {
            **super(FormElementUploadImage, self).json(),
            "label": self.label,
            "name": self.name,
            "default": self.default,
            "defaultValue": self.default
        }

    @classmethod
    def from_json(cls, obj):
        return FormElementUploadImage(**obj)
