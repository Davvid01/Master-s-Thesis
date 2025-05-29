import requests
from API_key_warszawa import api_key_warszawa
def fetch_parkingi_parknride():
    url=f"https://api.um.warszawa.pl/api/action/wfsstore_get?id=157648fd-a603-4861-af96-884a8e35b155&apikey={api_key_warszawa}"
    return api_key_warszawa
print(fetch_parkingi_parknride())