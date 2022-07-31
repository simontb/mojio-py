class Tires:

    def __init__(self, json_data):
        self.is_empty = False
        if json_data is None or len(json_data) == 0:
            self.is_empty = True
            return
        self.pressure_warning = json_data.get('TirePressureWarning', False)

    def getattribute(self, name: str, default: None):
        return getattr(self, name, default)
