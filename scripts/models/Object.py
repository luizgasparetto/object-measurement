import json

class Object:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
