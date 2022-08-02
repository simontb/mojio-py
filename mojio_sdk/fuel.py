class Fuel:

    def __init__(self, json_data):
        self.is_empty = False
        if json_data is None or len(json_data) == 0:
            self.is_empty = True
            return
        fuel_level_dict = json_data.get('FuelLevel', None)
        if fuel_level_dict is not None:
            self.fuel_level = fuel_level_dict.get('Value', 0.0)
        virtual_fuel_lvl_dict = json_data.get('VirtualFuelLevel', None)
        if virtual_fuel_lvl_dict is not None:
            self.virtual_fuel_level = virtual_fuel_lvl_dict.get('Value', 0.0)
        fuel_cap_dict = json_data.get('FuelCapacity', None)
        if fuel_cap_dict is not None:
            self.fuel_capacity = fuel_cap_dict.get('Value', 0.0)

    def getattribute(self, name: str, default=''):
        return getattr(self, name, default)
