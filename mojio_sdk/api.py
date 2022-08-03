from .authentication import Authentication
from .vehicle import Vehicle
from .trip import Trip
import requests


class API:

    def __init__(self, tenant, client_id, client_secret, username, password):
        self._tenant = tenant
        self._client_id = client_id
        self._client_secret = client_secret
        self._username = username
        self._password = password
        self._authentication = None

    def logged_in(self) -> bool:
        if self._authentication is None:
            return False
        else:
            return self._authentication.is_valid()

    def login(self) -> bool:
        payload = {
            'grant_type': 'password',
            'username': self._username,
            'password': self._password,
            'client_id': self._client_id,
            'client_secret': self._client_secret,
            'scope': 'full offline_access'
        }

        response = requests.post(self._get_auth_endpoint(), data=payload)

        self._authentication = Authentication()
        self._authentication.set_json(response.json())
        return self.logged_in()

    def get_vehicles(self) -> list[Vehicle]:
        return self._parse_devices(self._get_response("vehicles"))

    def get_trips(self) -> list[Trip]:
        return self._parse_trips(self._get_response("trips"))

    def get_trip(self, trip_id: str) -> Trip:
        return Trip(self._get_response("%s/%s" % ("trips", trip_id)))

    def _get_api_endpoint(self, service: str) -> str:
        return "https://%s-api.moj.io/v2/%s" % (self._tenant, service)

    def _get_auth_endpoint(self) -> str:
        return "https://%s-identity.moj.io/oauth2/token" % (self._tenant)

    def _get_response(self, service: str) -> dict:
        if self._authentication is None or not self._authentication.is_valid():
            self.login()

        auth_header = self._authentication.create_header()
        response = requests.get(self._get_api_endpoint(service), headers=auth_header)
        return response.json()

    @staticmethod
    def _parse_devices(json_data) -> list[Vehicle]:
        """Parse result from API."""
        result = []

        for json_vehicle_data in json_data['Data']:
            device = Vehicle(json_vehicle_data)
            result.append(device)

        return result

    @staticmethod
    def _parse_trips(json_data) -> list[Trip]:
        """Parse result from API."""
        result = []

        for json_trip_data in json_data['Data']:
            device = Trip(json_trip_data)
            result.append(device)

        return result
