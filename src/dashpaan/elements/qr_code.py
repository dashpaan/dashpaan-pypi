from src.dashpaan.elements.base import Element


class QrCode(Element):
    kind = "qr-code"

    size = "1.5*1.5"

    link = None
    title = None

    tabs = None

    def json(self):
        return {
            **super(QrCode, self).json(),
            "size": self.size,
            "link": self.link,
            "title": self.title,
            "tabs": self.tabs,
        }

    @classmethod
    def from_json(cls, obj):
        return QrCode(**obj)
