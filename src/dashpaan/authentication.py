from hashlib import sha256

from dashpaan.elements.base import Element


class Authentication(Element):
    kind = "authentication"

    role = "customer"
    name = "[Name]"
    username = "@username"
    profile = None
    token = None

    def json(self):
        return {
            **super(Authentication, self).json(),
            "access_token": self.token,
            "user": {
                "role": self.role,
                "uuid": sha256(self.username.encode()).hexdigest(),
                "data": {
                    "displayName": self.name,
                    "photoURL": self.profile,
                    "id": self.username,
                    "settings": {
                        "layout": {
                            "style": "layout1",
                            "config": {
                                "scroll": "content",
                                "navbar": {
                                    "display": True,
                                    "folded": True,
                                    "position": "left"
                                },
                                "toolbar": {
                                    "display": True,
                                    "style": "fixed",
                                    "position": "below"
                                },
                                "footer": {
                                    "display": True,
                                    "style": "fixed",
                                    "position": "below"
                                },
                                "mode": "fullwidth"
                            }
                        },
                        "customScrollbars": True,
                        "theme": {
                            "main": "green",
                            "navbar": "defaultDark",
                            "toolbar": "defaultDark",
                            "footer": "defaultDark"
                        }
                    },
                    "shortcuts": ["calendar", "mail", "contacts"]
                }
            }
        }

    @classmethod
    def from_json(cls, obj):
        return Authentication(**obj)
