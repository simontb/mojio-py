
class Seatbelt:

    def __init__(self, json_data):
        self.status_warning = False

        if 'Seatbelt' in json_data:
            self.status_warning = json_data['Seatbelt']['SeatbeltStatusWarning']
