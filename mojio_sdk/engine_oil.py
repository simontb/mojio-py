
class EngineOil:

    def __init__(self, json_data):
        self.level_warning = None
        self.low_pressure_warning = None
        self.temp = None

        if 'EngineOil' in json_data:
            eo = json_data['EngineOil']
            self.level_warning = eo['EngineOilLevelWarning']
            self.low_pressure_warning = eo['EngineOilPressureLowWarning']
            self.temp = eo['EngineOilTemperature']
