from .abstract_mojio import AbstractMojio


class Battery(AbstractMojio):

    def __init__(self, json_data):
        super().__init__(json_data)
        if not self.has_data:
            return
        self.connected = json_data.get('Connected', False)
        self.risk_severity = json_data.get('RiskSeverity', '')
        self.value = json_data.get('Value', 0.0)
        self.unit = json_data.get('Unit', None)
