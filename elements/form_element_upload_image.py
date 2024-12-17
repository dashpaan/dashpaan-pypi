import json

from dashpaan.elements.base import Element


class FormElementUploadImage(Element):
    kind = "formElementUploadImage"

    uri = ""
    title = ""
    data = []
    variables = {}

    def json(self):
        return {
            **super(FormElementUploadImage, self).json(),
            "uri": self.uri,
            "title": self.title,
            "data": self.data,
            "variables": self.variables
        }

    @classmethod
    def from_json(cls, obj):
        return FormElementUploadImage(**obj)