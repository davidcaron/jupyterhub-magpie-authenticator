from traitlets import Unicode
from jupyterhub.auth import Authenticator
from tornado import gen
import requests


class MagpieAuthenticator(Authenticator):
    default_provider = "ziggurat"
    magpie_url = Unicode(
        default_value="https://www.example.com/magpie",
        config=True,
        help="Magpie endpoint to signin to"
    )

    @gen.coroutine
    def authenticate(self, handler, data):
        signin_url = self.magpie_url.rstrip('/') + '/signin'
        
        post_data = {
            "user_name": data["username"],
            "password": data["password"],
            "provider_name": self.default_provider,
        }
        response = requests.post(signin_url, data=post_data)
        
        if response.ok:
            return data['username']
