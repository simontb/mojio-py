class AbstractMojio():
    def __init__(self, json_data: dict):
        self.has_data = True
        self.raw_json = json_data
        if json_data is None or len(json_data) == 0:
            self.has_data = False

    def getattribute(self, name: str, default=''):
        return getattr(self, name, default)
