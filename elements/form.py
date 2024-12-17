import json

from dashpaan.elements.base import Element


class Form(Element):
    kind = "form"

    uri = ""
    title = ""
    data = []
    variables = {}
    fields = []
    buttons = []

    def json(self):
        return {
            **super(Form, self).json(),
            "uri": self.uri,
            "title": self.title,
            "data": self.data,
            "variables": self.variables,
            "fields": self.fields,
            "buttons": self.buttons
        }

    @classmethod
    def from_json(cls, obj):
        return Form(**obj)