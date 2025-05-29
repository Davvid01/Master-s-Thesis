import requests
from API_key_warszawa import api_key_warszawa
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
def fetch_parkingi_parknride():
    url=f"https://api.um.warszawa.pl/api/action/wfsstore_get?id=157648fd-a603-4861-af96-884a8e35b155&apikey={api_key_warszawa}"
    response = requests.get(url).json()
    records = response.get("result", {}).get("featureMemberProperties",{})
    coordinates = response.get("result", {}).get("featureMemberList",{})
    to_df=pd.DataFrame(records)
    coord_df=pd.DataFrame(coordinates)
    return coord_df, to_df
print(fetch_parkingi_parknride())