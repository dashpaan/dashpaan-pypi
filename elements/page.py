import json

from dashpaan.elements.base import Element


class Page(Element):
    kind = "page"

    uri = ""
    title = ""
    data = []
    variables = {}
    templates = {}
    elements = []
    navigation = {}

    def json(self):
        return {
            **super(Page, self).json(),
            "uri": self.uri,
            "title": self.title,
            "data": self.data,
            "variables": self.variables,
            "templates": self.templates,
            "elements": [element for element in self.elements],
            "navigation": self.navigation
        }

    @classmethod
    def from_json(cls, obj):
        return Page(**obj)