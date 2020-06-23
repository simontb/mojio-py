from .location import Location


class Vehicle:

    def __init__(self, json_data):
        self.licence_plate = json_data['LicensePlate']
        self.location = Location(json_data['Location'])
