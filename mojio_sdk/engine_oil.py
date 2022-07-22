class EngineOil:

    def __init__(self, json_data):
        self.level_warning = json_data.get('EngineOilLevelWarning')
        self.low_pressure_warning = json_data.get('EngineOilPressureLowWarning', False)
        self.temp = json_data.get('EngineOilTemperature', 0.0)
