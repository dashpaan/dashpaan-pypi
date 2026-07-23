import json

from dashpaan.elements.base import Element


class WYSIWYGEditor(Element):
    kind = "wysiwyg-editor"

    name = ""
    content = ""
    default = ""
    label = ""

    def json(self):
        return {
            **super(WYSIWYGEditor, self).json(),
            "name": self.name,
            "content": self.content,
            "label": self.label,
            "default": self.default,
            "defaultValue": self.default,
        }

    @classmethod
    def from_json(cls, obj):
        return WYSIWYGEditor(**obj)
