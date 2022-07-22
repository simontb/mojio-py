class Fuel:

    def __init__(self, json_data):
        self.fuel_level = json_data.get('FuelLevel').get('Value', 0.0)
        self.fuel_capacity = json_data.get('FuelCapacity').get('Value', 0.0)
