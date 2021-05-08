import time


class Authentication(object):
    """Object used to store, load and validate authentication information."""

    def __init__(self):
        """Initialize RitAssistAuthentication object."""
        self.access_token = None
        self.refresh_token = None
        self.authenticated = None
        self.expires_in = None

    @property
    def token(self):
        """Return the access token."""
        return self.access_token

    def set_json(self, json):
        """Set all attributes based on JSON response."""
        if 'access_token' in json:
            self.authenticated = time.time()
            self.access_token = json['access_token']
            self.refresh_token = json['refresh_token']
            self.expires_in = json['expires_in']
        else:
            self.access_token = None

    def create_header(self):
        """Return an authorization header."""
        return {'Authorization': 'Bearer ' + self.access_token}

    def is_valid(self):
        """Check if the access token is still valid."""
        if self.access_token is None or self.expires_in is None or self.authenticated is None:
            return False

        current = time.time()
        expire_time = self.authenticated + self.expires_in

        return expire_time > current + 10
