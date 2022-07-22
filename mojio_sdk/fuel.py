class Fuel:

    def __init__(self, json_data):
        self.fuel_level = None
        self.fuel_capacity = None

        if 'FuelLevel' in json_data:
            self.fuel_level = json_data['FuelLevel']
        if 'FuelCapacity' in json_data:
            self.fuel_capacity = json_data['FuelCapacity']
