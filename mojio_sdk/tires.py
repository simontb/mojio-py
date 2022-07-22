class Tires:

    def __init__(self, json_data):
        self.pressure = None

        if 'TirePressure' in json_data:
            self.pressure = json_data['TirePressure']
