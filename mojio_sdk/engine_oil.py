class EngineOil:

    def __init__(self, json_data):
        self.level_warning = json_data.get('EngineOilLevelWarning')
        self.low_pressure_warning = json_data.get('EngineOilPressureLowWarning', False)
        self.temp = json_data.get('EngineOilTemperature').get('Value', 0.0)
        self.temp_units = json_data.get('EngineOilTemperature').get('Unit', '')
        self.temp_c = 0.0
        self.temp_f = 0.0
        if 'celsius' in self.temp_units.lower():
            self.temp_c = self.temp
            self.temp_f = (self.temp_c * 1.8) + 32
        else:
            self.temp_f = self.temp
            self.temp_c = (self.temp_f - 32) * 1.8
