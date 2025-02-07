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

url="https://bip.poznan.pl/api-json/bip/oferty-pracy/"
response=requests.get(url)
data=response.json()
print(data)


structuring=data['bip.poznan.pl']#['data']['oferta_pracy']['items']['oferta']
print(data.keys())
print(structuring.keys()) #sprawdzam keys w słowniku z API
frame=pd.DataFrame(data)
print(frame)
frame.info()
for k,v in structuring.items():
    print(f'{k} oraz {v}')
    for x in v:
        print(x)
        for klucz, wartosc in x.items():
            print(f"Wartościa w slowniku data jest: {wartosc}")
            print(f'Items: {wartosc['items']}')
            for oferty in wartosc['items']:
                print(oferty)
                for kl, wart in oferty.items():
                    print(wart)
                    for q in wart:
                        print(f'Oferty pracy w poznaniu to: {q}')
                    test=pd.DataFrame(wart)
                    #test.to_csv('praca1.csv', index_col=0)
print(test)
for lab, row in test.iterrows():
    print(lab)
    print(row)