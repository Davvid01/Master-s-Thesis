from db.connect import create_db_engine
from db.sql_writer import write_to_sql

from api_clients.Wroclaw_API_komunikacja_miejska import fetch_cennik_WRM, fetch_lokalizacja_pojazdow_komunikacji
from data_processing.wroclaw_processor import process_cennik_wrm, process_lokalizacja_pojazdow_wroc

import pandas as pd

def main():
    # Połączenie z bazą danych
    engine = create_db_engine()

    # 1. Wrocław – pobierz dane
    raw_data = fetch_cennik_WRM()
    raw_data2= fetch_lokalizacja_pojazdow_komunikacji()
    # 2. Przetwórz dane
    df = process_cennik_wrm(raw_data)
    df= df[['_id','Column1','Column2','Column3']]
    df_lokalizacja_pojazdow=process_lokalizacja_pojazdow_wroc(raw_data2)
    df_lokalizacja_pojazdow=df_lokalizacja_pojazdow[["_id","Nr_Boczny","Nr_Rej","Brygada","Nazwa_Linii","Ostatnia_Pozycja_Szerokosc","Ostatnia_Pozycja_Dlugosc","Data_Aktualizacji"]]
    # 3. Zapisz do SQL
    write_to_sql(df, engine, "WroclawCennikWrm")

    print("Dane z Wrocławia zostały zapisane do bazy danych.")
    print(df_lokalizacja_pojazdow.columns.values)
    pd.set_option('display.max_columns', None)
    print(df_lokalizacja_pojazdow)

if __name__ == "__main__":
    main()
