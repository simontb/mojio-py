from .abstract_mojio import AbstractMojio


class Dtc(AbstractMojio):

    def __init__(self, dtc_code_list: list):
        self.has_data = True
        self.count = len(dtc_code_list)
        self.details = []
        if dtc_code_list is None or self.count == 0:
            self.has_data = False
            return
        for dtc in dtc_code_list:
            self.details.append({"timestamp": dtc.get('Timestamp', ''),
                                 "code": dtc.get('Code', ''),
                                 "desc": dtc.get('Description', ''),
                                 "type": dtc.get('Type', ''),
                                 "state_type": dtc.get('StateType', ''),
                                 "severity": dtc.get('Severity', ''),
                                 "ignored": dtc.get('Ignored', '')})
