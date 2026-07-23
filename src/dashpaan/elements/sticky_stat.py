import json

from dashpaan.elements.base import Element


class StickyStat(Element):
    kind = "sticky-stat"

    title = None
    value = 0
    color = "#000"
    size = "1*1"

    def json(self):
        return {
            **super(StickyStat, self).json(),
            "version": self.version,
            "size": self.size,
            "value": self.value,
            "color": self.color,
            "title": self.title
        }

    @classmethod
    def from_json(cls, obj):
        return StickyStat(**obj)
