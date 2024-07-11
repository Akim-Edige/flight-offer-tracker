import requests
import os


class Getiata:

    def __init__(self):
        self.api_key = os.environ["API_KEY"]
        self.api_secret = os.environ["API_SECRET"]
        self.server = "https://test.api.amadeus.com/v1"

        self.token = self.get_token()


    def get_token(self):

        u=f"{self.server}/security/oauth2/token"
        auth={
            "Content-Type": "application/x-www-form-urlencoded"
        }
        d = {
            "grant_type":"client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }

        response = requests.post(url=u, data=d, headers=auth)

        return response.json()["access_token"]


    def get_city(self, city):

        u = f"{self.server}/reference-data/locations/cities"

        d = {
            "keyword" : city,
            "max" : 10
        }

        auth = {
            "Authorization" : f"Bearer {self.token}"
        }

        res = requests.get(url = u, params = d, headers = auth)

        return (res.json()["data"][0]["iataCode"])
