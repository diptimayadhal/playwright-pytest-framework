import requests
from utils.config_reader import load_config
import re

config = load_config()

BASE_URL = config["api_base_url"]

class OrangeHRMClient:

    def __init__(self):
        self.session = requests.Session()

    def login(self, username, password):

        # Step 1: Get login page
        response = self.session.get(f"{BASE_URL}/web/index.php/auth/login")

        # Extract CSRF token
        token_match = re.search(
            r'name="_token" value="(.*?)"',
            response.text
        )

        token = token_match.group(1)

        # Step 2: Login request
        payload = {
            "_token": token,
            "username": username,
            "password": password
        }

        login_response = self.session.post(
            f"{BASE_URL}/web/index.php/auth/validate",
            data=payload
        )

        return login_response