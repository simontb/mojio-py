from .location import Location
from .fuel import Fuel
from .engine_oil import EngineOil
from .tires import Tires
from .battery import Battery
from .dtc import Dtc


class Vehicle:

    def __init__(self, json_data):
        self.is_empty = False
        if json_data is None or len(json_data) == 0:
            self.is_empty = True
            return
        # Info
        self.raw_json = json_data
        self.licence_plate = json_data.get('LicensePlate', '')
        self.vin = json_data.get('DetectedVIN', None)
        if self.vin == '' or self.vin is None:
            self.vin = json_data.get('VIN')
        if self.licence_plate == '':
            self.id = self.vin
        else:
            self.id = self.licence_plate.replace("-", "_").replace(" ", "_")
        self.mojio_id = json_data.get('Id')
        self.last_contact = json_data.get('LastContactTime')
        self.last_modified = json_data.get('LastModified')
        self.name = None
        vin_dict = json_data.get('VinDetails', None)
        if vin_dict is not None:
            self.name = '%s %s %s' % (vin_dict.get('Year', ''), vin_dict.get('Make', ''), vin_dict.get('Model', ''))
        self.last_trip_id = json_data.get('LastTripId', '')
        # Ignition State
        self.ignition_state = False
        ignition_state_dict = json_data.get('IgnitionState', None)
        if ignition_state_dict is not None:
            self.ignition_state = ignition_state_dict.get('Value', False)
        # Speed and RPM
        current_speed = json_data.get('Speed').get('Value', None)
        self.current_rpm_unit = json_data.get('RPM').get('Unit', '')
        self.current_speed_unit = json_data.get('Speed').get('Unit', '')
        if current_speed is not None and self.ignition_state:
            self.current_rpm = json_data.get('RPM').get('Value', None)
            if 'kilometers' in self.current_speed_unit.lower():
                self.current_speed_kph = current_speed
                self.current_speed_mph = float(self.current_speed_kph) / 1.609
            else:
                self.current_speed_mph = current_speed
                self.current_speed_kph = float(self.current_speed_mph) * 1.609
        else:
            self.current_rpm = None
            self.current_speed_kph = None
            self.current_speed_mph = None
        # Parked and motion
        self.parked = json_data.get('ParkedState').get('Value', 'unknown')
        self.status = json_data.get('VehicleStatus').get('Value', 'unknown')
        # Heading and Turn
        heading = json_data.get('Heading', None)
        if heading is not None:
            self.heading_direction = heading.get('Direction', '')
            self.left_turn = heading.get('LeftTurn', False)
        # Idle State
        idle_state = json_data.get('IdleState', None)
        if idle_state is not None:
            self.idle = idle_state.get('Value', False)
        # Tow State
        tow_state_dict = json_data.get('TowState', None)
        if tow_state_dict is not None:
            self.tow_state = tow_state_dict.get('Value', False)
        # Disturbance
        disturbance_state_dict = json_data.get('DisturbanceState', None)
        if disturbance_state_dict is not None:
            self.disturbance_state = disturbance_state_dict.get('Value', False)
        # Seatbelt
        sb_dict = json_data.get('Seatbelt')
        if sb_dict is not None:
            self.seatbelt_status_warning = sb_dict.get('SeatbeltStatusWarning', False)
        # Build other objects
        self.location = Location(json_data.get('Location', None))
        self.fuel = Fuel(json_data)
        self.engine_oil = EngineOil(json_data.get('EngineOil', None))
        self.tires = Tires(json_data.get('TirePressure', None))
        self.battery = Battery(json_data.get('Battery', None))
        self.dtc = Dtc(json_data.get('DiagnosticCodes', None))

    def getattribute(self, name: str, default=''):
        return getattr(self, name, default)
