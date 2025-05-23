import requests

def fetch_cennik_WRM():
    url = "https://www.wroclaw.pl/open-data/api/action/datastore_search?resource_id=398b3a07-b697-4b6a-9029-64154b07cf53"
    response = requests.get(url)
    return response.json()

def fetch_lokalizacja_pojazdow_komunikacji():
    url = "https://www.wroclaw.pl/open-data/api/action/datastore_search?resource_id=a9b3841d-e977-474e-9e86-8789e470a85a"
    response = requests.get(url)
    return response.json()
