from dashpaan.elements.base import Element


class DonutChart(Element):
    kind = "donut-chart"

    title = ""
    size = "1*1"
    series = {}
    labels = []

    def json(self):
        return {
            **super(DonutChart, self).json(),
            "version": self.version,
            "title": self.title,
            "size": self.size,
            "series": self.series,
            "labels": self.labels
        }

    @classmethod
    def from_json(cls, obj):
        return DonutChart(**obj)
