class Location:

    def __init__(self, json_data):
        self.is_empty = False
        if json_data is None or len(json_data) == 0:
            self.is_empty = True
            return
        self.latitude = json_data.get('Lat')
        self.longitude = json_data.get('Lng')
        self.address = json_data.get('Address')
        self.formatted_address = ''
        if self.address is not None:
            self.formatted_address = self.address.get('FormattedAddress', '')

    def getattribute(self, name: str, default=''):
        return getattr(self, name, default)
