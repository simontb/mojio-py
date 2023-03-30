from .abstract_mojio import AbstractMojio


class Location(AbstractMojio):

    def __init__(self, json_data):
        super().__init__(json_data)
        if not self.has_data:
            return
        self.latitude = json_data.get('Lat')
        self.longitude = json_data.get('Lng')
        self.address = json_data.get('Address')
        self.formatted_address = ''
        if self.address is not None:
            self.formatted_address = self.address.get('FormattedAddress', '')
