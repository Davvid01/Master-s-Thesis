import pyodbc
import requests
import pandas as pd
from sqlalchemy import create_engine
#from sqlalchemy import create_engine
print(pyodbc.drivers())
import urllib.parse  # Poprawiono import

# Definicja ciągu połączenia do pyodbc
conn_str = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=VICTUS\\SQLEXPRESS;"
    "Database=Baza_API;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

# Kodowanie ciągu połączenia do SQLAlchemy
params = urllib.parse.quote_plus(conn_str)

# Tworzenie SQLAlchemy engine
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
# Pobieranie danych z API
url = "https://api.um.warszawa.pl/api/action/get_companies/?apikey=ca30886e-6f6f-435a-8b36-4468de811529&resource_id=2aa01577-9f24-4b8e-83f5-d3d15f6d094b"
response = requests.get(url)
data = response.json()
#print(data)

structuring = data['result']['Items']['ComboItem']
#print(structuring)
frejm = pd.DataFrame(structuring)
print(frejm)

frejm.to_sql("ExampleTable", con=engine, if_exists="replace", index=False)
