import webbrowser
import requests
import time


def _ensure_single_slash(url):
    if url.endswith("/"):
        return url
    else:
        return url + "/"


class MolgenisAuthClient:
    auth_server = None
    endpoint = None
    scopes = None
    client_id = None

    def __init__(self, auth_server, client_id, scopes):
        self.auth_server = auth_server
        self.scopes = scopes
        self.client_id = client_id
        self._discover()

    def _discover(self):
        response = requests.get(_ensure_single_slash(self.auth_server) + ".well-known/openid-configuration")
        response.raise_for_status()
        configuration = response.json()
        self.endpoint = {
            "authorize": configuration["authorization_endpoint"],
            "access": configuration["token_endpoint"],
            "user": configuration["userinfo_endpoint"],
            "device": configuration["device_authorization_endpoint"],
            "logout": configuration["end_session_endpoint"]
        }

    def request_device_code(self):
        auth_response = requests.post(self.endpoint["device"], data={
            "client_id": self.client_id,
            "scope": self.scopes
        })
        auth_response.raise_for_status()
        auth_data = auth_response.json()
        return auth_data

    def open_browser_for_client(self, url, code):
        print("Open this code:", code)
        webbrowser.open(f'{url}&client_id={self.client_id}')

    def request_token(self, auth_data):
        return requests.post(self.endpoint['access'], data={
            "scope": self.scopes,
            "client_id": self.client_id,
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
            "device_code": auth_data["device_code"]
        })

    def device_flow_auth(self):
        auth_data = self.request_device_code()
        self.open_browser_for_client(auth_data['verification_uri_complete'], auth_data['user_code'])
        interval = auth_data["interval"]
        expires_in = auth_data["expires_in"]
        deadline = time.time() + expires_in

        while time.time() < deadline:
            data = self.request_token(auth_data).json()

            if "error" not in data:
                return data

            if data["error"] == "authorization_pending":
                time.sleep(interval)
                continue

            # If the server tells us to back off longer
            if data["error"] == "slow_down":
                interval += 5
                time.sleep(interval)
                continue

            # If it's any other error, stop
            raise Exception(f"OAuth error: {data}")

        raise TimeoutError("Authorization timed out")


if __name__ == '__main__':
    # set this in .env or something?
    client = MolgenisAuthClient("https://auth.molgenis.org", "b396233b-cdb2-449e-ac5c-a0d28b38f791",
                                "openid offline_access")
    auth = client.device_flow_auth()
    print(auth)
