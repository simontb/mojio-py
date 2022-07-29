class Fuel:

    def __init__(self, json_data):
        if json_data is None:
            return
        self.fuel_level = 0.0
        self.virtual_fuel_level = 0.0
        self.fuel_capacity = 0.0
        if json_data.get('FuelLevel') is not None:
            self.fuel_level = json_data.get('FuelLevel').get('Value', 0.0)
        if json_data.get('VirtualFuelLevel') is not None:
            self.virtual_fuel_level = json_data.get('VirtualFuelLevel').get('Value', 0.0)
        if json_data.get('FuelCapacity') is not None:
            self.fuel_capacity = json_data.get('FuelCapacity').get('Value', 0.0)

    def getattribute(self, name: str, default=''):
        return getattr(self, name, default)
