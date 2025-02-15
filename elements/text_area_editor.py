import json

from dashpaan.elements.base import Element


class TextAreaEditor(Element):
    kind = "text-area-editor"

    defaultValue = ""
    name = ""
    label = ""

    def json(self):
        return {
            **super(TextAreaEditor, self).json(),
            "name": self.name,
            "label": self.label,
            "defaultValue": self.defaultValue,
        }

    @classmethod
    def from_json(cls, obj):
        return TextAreaEditor(**obj)
