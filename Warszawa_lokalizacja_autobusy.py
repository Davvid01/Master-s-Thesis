import requests
import pandas as pd
from sqlalchemy import create_engine, inspect
import urllib

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


url="https://api.um.warszawa.pl/api/action/busestrams_get/?resource_id=f2e5503e-927d-4ad3-9500-4ab9e55deb59&apikey=ca30886e-6f6f-435a-8b36-4468de811529&type=2"
response=requests.get(url)
data=response.json()
#print(data)

structuring=data['result']
#print(structuring)
df=pd.DataFrame(structuring)
#print(df)
df.info()

df.to_sql("BussesTrams", con=engine, if_exists="replace", index=False)