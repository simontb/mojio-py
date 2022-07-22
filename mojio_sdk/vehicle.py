from .location import Location
from .fuel import Fuel
from .engine_oil import EngineOil
from .tires import Tires
from .battery import Battery
from .seatbelt import Seatbelt


class Vehicle:

    def __init__(self, json_data):
        self.current_rpm = json_data.get('RPM').get('Value', 0)
        self.current_rpm_unit = json_data.get('RPM').get('Unit', '')
        self.current_speed = json_data.get('Speed').get('Value', 0)
        self.current_speed_unit = json_data.get('Speed').get('Value', '')
        self.parked = json_data.get('ParkedState').get('Value', 'unknown')
        self.status = json_data.get('VehicleStatus').get('Value', 'unknown')
        self.licence_plate = json_data.get('LicensePlate')
        self.vin = json_data.get('DetectedVIN')
        self.last_contact = json_data.get('LastContactTime')
        self.last_modified = json_data.get('LastModified')
        self.name = None
        if 'VinDetails' in json_data:
            vin = json_data['VinDetails']
            self.name = '%s %s %s' % (vin.get('Year', ''), vin.get('Make', ''), vin.get('Model', ''))
        self.location = Location(json_data.get('Location'))
        self.fuel = Fuel(json_data)
        self.engine_oil = EngineOil(json_data.get('EngineOil'))
        self.tires = Tires(json_data.get('TirePressure'))
        self.battery = Battery(json_data.get('Battery'))
        self.seatbelt = Seatbelt(json_data.get('Seatbelt'))
