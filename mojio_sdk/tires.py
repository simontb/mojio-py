class Tires:

    def __init__(self, json_data):
        self.pressure_warning = json_data.get('TirePressureWarning', False)
