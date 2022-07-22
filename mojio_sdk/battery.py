class Battery:

    def __init__(self, json_data):
        self.connected = False
        self.risk_severity = None
        self.value = 0.0
        self.unit = None

        if 'Battery' in json_data:
            battery = json_data['Battery']
            self.connected = battery['Connected']
            self.risk_severity = battery['RiskSeverity']
            self.value = battery['Value']
            self.unit = battery['Unit']
