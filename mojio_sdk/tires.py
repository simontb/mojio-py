from .abstract_mojio import AbstractMojio


class Tires(AbstractMojio):

    def __init__(self, json_data):
        super().__init__(json_data)
        if not self.has_data:
            return
        self.pressure_warning = json_data.get('TirePressureWarning', False)
