from dashpaan.elements.base import Element


class Page(Element):
    kind = "page"

    uri = ""
    title = ""
    data = []
    variables = {}
    templates = {}
    elements = []
    navigation = "keep"
    authentication = "keep"

    def json(self):
        return {
            **super(Page, self).json(),
            "uri": self.uri,
            "title": self.title,
            "data": self.data,
            "variables": self.variables,
            "templates": self.templates,
            "elements": [element.json() for element in self.elements],
            "navigation": self.navigation.json() if hasattr(self.navigation, "json") else self.navigation,
            "authentication": self.authentication.json() if
            hasattr(self.authentication, "json") else self.authentication
        }

    @classmethod
    def from_json(cls, obj):
        return Page(**obj)
