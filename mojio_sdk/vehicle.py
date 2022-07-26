from .location import Location
from .fuel import Fuel
from .engine_oil import EngineOil
from .tires import Tires
from .battery import Battery
from .seatbelt import Seatbelt


class Vehicle:

    def __init__(self, json_data):
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
        self.heading_direction = ''
        self.left_turn = False
        if json_data.get('Heading') is not None:
            heading = json_data.get('Heading')
            self.heading_direction = heading.get('Direction', '')
            self.left_turn = heading.get('LeftTurn', False)
        self.idle = False
        if json_data.get('IdleState') is not None:
            self.idle = json_data.get('IdleState').get('Value', False)
        self.ignition_state = False
        if json_data.get('IgnitionState') is not None:
            self.ignition_state = json_data.get('IgnitionState').get('Value', False)
        self.tow_state = False
        if json_data.get('TowState') is not None:
            self.tow_state = json_data.get('TowState').get('Value', False)
        self.disturbance_state = False
        if json_data.get('DisturbanceState') is not None:
            self.disturbance_state = json_data.get('DisturbanceState').get('Value', False)
        # Info
        self.licence_plate = json_data.get('LicensePlate')
        self.vin = json_data.get('DetectedVIN')
        self.last_contact = json_data.get('LastContactTime')
        self.last_modified = json_data.get('LastModified')
        self.name = None
        if 'VinDetails' in json_data:
            vin = json_data['VinDetails']
            self.name = '%s %s %s' % (vin.get('Year', ''), vin.get('Make', ''), vin.get('Model', ''))
        # Build other objects
        self.location = Location(json_data.get('Location'))
        self.fuel = Fuel(json_data)
        self.engine_oil = EngineOil(json_data.get('EngineOil'))
        self.tires = Tires(json_data.get('TirePressure'))
        self.battery = Battery(json_data.get('Battery'))
        self.seatbelt = Seatbelt(json_data.get('Seatbelt'))
