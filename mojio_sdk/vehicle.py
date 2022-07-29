from .location import Location
from .fuel import Fuel
from .engine_oil import EngineOil
from .tires import Tires
from .battery import Battery


class Vehicle:

    def __init__(self, json_data):
        if json_data is None:
            return
        # Speed and RPM
        self.current_rpm = json_data.get('RPM').get('Value', 0)
        self.current_rpm_unit = json_data.get('RPM').get('Unit', '')
        self.current_speed_kph = 0
        self.current_speed_mph = 0
        self.current_speed_unit = json_data.get('Speed').get('Unit', '')
        if 'kilometers' in self.current_speed_unit.lower():
            self.current_speed_kph = json_data.get('Speed').get('Value', 0)
            self.current_speed_mph = float(self.current_speed_kph) / 1.609
        else:
            self.current_speed_mph = json_data.get('Speed').get('Value', 0)
            self.current_speed_kph = float(self.current_speed_mph) * 1.609
        # Parked and motion
        self.parked = json_data.get('ParkedState').get('Value', 'unknown')
        self.status = json_data.get('VehicleStatus').get('Value', 'unknown')
        # Heading and Turn
        self.heading_direction = ''
        self.left_turn = False
        heading = json_data.get('Heading', None)
        if heading is not None:
            self.heading_direction = heading.get('Direction', '')
            self.left_turn = heading.get('LeftTurn', False)
        # Idle State
        self.idle = False
        idle_state = json_data.get('IdleState', None)
        if idle_state is not None:
            self.idle = idle_state.get('Value', False)
        # Ignition State
        self.ignition_state = False
        ignition_state_dict = json_data.get('IgnitionState', None)
        if ignition_state_dict is not None:
            self.ignition_state = ignition_state_dict.get('Value', False)
        # Tow State
        self.tow_state = False
        tow_state_dict = json_data.get('TowState', None)
        if tow_state_dict is not None:
            self.tow_state = tow_state_dict.get('Value', False)
        # Disturbance
        self.disturbance_state = False
        disturbance_state_dict = json_data.get('DisturbanceState', None)
        if disturbance_state_dict is not None:
            self.disturbance_state = disturbance_state_dict.get('Value', False)
        # Info
        self.licence_plate = json_data.get('LicensePlate', '')
        self.vin = json_data.get('DetectedVIN')
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
        self.trips = None
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

    def getattribute(self, name: str, default=''):
        return getattr(self, name, default)
