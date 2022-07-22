from .location import Location
from .fuel import Fuel
from .engine_oil import EngineOil
from .tires import Tires
from .battery import Battery
from .seatbelt import Seatbelt


class Vehicle:

    def __init__(self, json_data):
        self.current_rpm = None
        self.current_rpm_unit = None
        self.current_speed = None
        self.current_speed_unit = None
        self.parked = None
        self.status = None
        self.licence_plate = json_data['LicensePlate']
        self.vin = json_data['DetectedVIN']
        self.last_contact = json_data['LastContactTime']
        self.last_modified = json_data['LastModified']
        if 'ParkedState' in json_data:
            self.parked = json_data['ParkedState']['Value']
        if 'VehicleStatus' in json_data:
            self.status = json_data['VehicleStatus']['Value']
        if 'RPM' in json_data:
            rpm = json_data['RPM']
            self.current_rpm = rpm['Value']
            self.current_rpm_unit = rpm['Unit']
        if 'Speed' in json_data:
            speed = json_data['Speed']
            self.current_speed = speed['Value']
            self.current_speed_unit = speed['Unit']
        self.location = Location(json_data['Location'])
        self.fuel = Fuel(json_data)
        self.engine_oil = EngineOil(json_data)
        self.tires = Tires(json_data)
        self.battery = Battery(json_data)
        self.seatbelt = Seatbelt(json_data)
