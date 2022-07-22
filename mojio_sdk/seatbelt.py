class Seatbelt:

    def __init__(self, json_data):
        self.status_warning = json_data.get('SeatbeltStatusWarning', False)
