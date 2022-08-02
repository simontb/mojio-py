class EngineOil:

    def __init__(self, json_data):
        self.is_empty = False
        if json_data is None or len(json_data) == 0:
            self.is_empty = True
            return
        self.level_warning = json_data.get('EngineOilLevelWarning', 'None')
        self.low_pressure_warning = json_data.get('EngineOilPressureLowWarning', False)
        oil_temp_key = json_data.get('EngineOilTemperature', None)
        if oil_temp_key is not None:
            temp = oil_temp_key.get('Value', 0.0)
            self.temp_units = oil_temp_key.get('Unit', '')
            if 'celsius' in self.temp_units.lower():
                self.temp_c = temp
                self.temp_f = (self.temp_c * 1.8) + 32
            else:
                self.temp_f = temp
                self.temp_c = (self.temp_f - 32) * 1.8

    def getattribute(self, name: str, default=''):
        return getattr(self, name, default)
