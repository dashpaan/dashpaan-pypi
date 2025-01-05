import json

from dashpaan.elements.base import Element


class Form(Element):
    kind = "form"

    uri = ""
    title = ""
    data = [
                    {
                        "id": "01ff61ca-2e47-4ebe-b076-7aa9491fcbcb",
                        "payload": {},
                        "headers": {},
                        "url": ""
                    }
                ]
    variables = {
                    "bookName": "The Hard Things about Hard Things",
                    "categoryId": 87564521
                }
    fields = []
    buttons = []

    def json(self):
        return {
            **super(Form, self).json(),
            "uri": self.uri,
            "title": self.title,
            "data": self.data,
            "variables": self.variables,
            "fields": [field.json() for field in self.fields],
            "buttons": [button.json() for button in self.buttons]
        }

    @classmethod
    def from_json(cls, obj):
        return Form(**obj)