import json

from dashpaan.elements.base import Element


class QrCode(Element):
    kind = "qr_code"

    size = "1.5*1.5"
    link = None
    tabs = None

    def json(self):
        return {
            **super(QrCode, self).json(),
            "url": self.url,
            "link": self.link,
            "tabs": self.tabs,
        }

    @classmethod
    def from_json(cls, obj):
        return QrCode(**obj)
