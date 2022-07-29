class Tires:

    def __init__(self, json_data):
        if json_data is None:
            return
        self.pressure_warning = json_data.get('TirePressureWarning', False)

    def getattribute(self, name: str, default: None):
        return getattr(self, name, default)
