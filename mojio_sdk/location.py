class Location:

    def __init__(self, json_data):
        self.latitude = json_data['Lat']
        self.longitude = json_data['Lng']
        self.address = None
        if 'Address' in json_data:
            self.address = json_data['Address']
