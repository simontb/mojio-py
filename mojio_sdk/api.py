from .authentication import Authentication
from .vehicle import Vehicle
import requests


class API:

    def __init__(self, tenant, client_id, client_secret, username, password):
        self._tenant = tenant
        self._client_id = client_id
        self._client_secret = client_secret
        self._username = username
        self._password = password
        self._authentication = None

    def logged_in(self):
        if self._authentication is None:
            return False
        else:
            return self._authentication.is_valid()

    def login(self):
        auth_url = "https://" + self._tenant + "-identity.moj.io/oauth2/token"

        payload = {
            'grant_type': 'password',
            'username': self._username,
            'password': self._password,
            'client_id': self._client_id,
            'client_secret': self._client_secret,
            'scope': 'full offline_access'
        }

        response = requests.post(auth_url, data=payload)

        self._authentication = Authentication()
        self._authentication.set_json(response.json())
        return self.logged_in()

    def get_vehicles(self):
        if self._authentication is None or not self._authentication.is_valid():
            return []

        data_url = "https://" + self._tenant + "-api.moj.io/v2/vehicles"

        auth_header = self._authentication.create_header()
        response = requests.get(data_url, headers=auth_header)
        data = response.json()
        return self._parse_devices(data)

    @staticmethod
    def _parse_devices(json_data):
        """Parse result from API."""
        result = []

        for json_vehicle_data in json_data['Data']:
            device = Vehicle(json_vehicle_data)
            result.append(device)

        return result
