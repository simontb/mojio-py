class Location:

    def __init__(self, json_data):
        self.latitude = json_data.get('Lat')
        self.longitude = json_data.get('Lng')
        self.address = json_data.get('Address')
        self.formatted_address = ''
        if self.address is not None:
            self.formatted_address = json_data.get('Address').get('FormattedAddress', '')
