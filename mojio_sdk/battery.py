class Battery:

    def __init__(self, json_data):
        if json_data is None:
            return
        self.connected = json_data.get('Connected', False)
        self.risk_severity = json_data.get('RiskSeverity')
        self.value = json_data.get('Value', 0.0)
        self.unit = json_data.get('Unit')

    def getattribute(self, name: str, default=''):
        return getattr(self, name, default)
