from dashpaan.elements.base import Element


class DataTable(Element):
    kind = "data-table"

    uri = ""
    title = ""
    size = "4*3"
    errors = {}
    columns = []
    rows = []

    def json(self):
        return {
            **super(DataTable, self).json(),
            "uri": self.uri,
            "title": self.title,
            "errors": self.errors,
            "columns": self.columns,
            "rows": self.rows,
            "size": self.size
        }

    @classmethod
    def from_json(cls, obj):
        return DataTable(**obj)
