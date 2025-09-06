import requests
import pandas as pd
from sqlalchemy import create_engine, inspect
import urllib

# Wczytaj klucz API z pliku tekstowego
def load_api_key(filepath):
    try:
        with open(filepath, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        exit(1)

# Ścieżka do pliku z kluczem API
api_key_path = "api_key.txt"
api_key = load_api_key(api_key_path)


conn_str = urllib.parse.quote_plus(
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=VICTUS\\SQLEXPRESS;"
    "Database=Baza_API;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={conn_str}")

inspector = inspect(engine)
print(inspector.get_table_names())


url=f"https://api.um.warszawa.pl/api/action/busestrams_get/?resource_id=f2e5503e-927d-4ad3-9500-4ab9e55deb59&apikey={api_key}&type=1"
response=requests.get(url)
data=response.json()
#print(data)

structuring=data['result']
#print(structuring)
df=pd.DataFrame(structuring)
#print(df)
df.info()
print(df)
df.to_sql("BussesTrams", con=engine, if_exists="replace", index=False)