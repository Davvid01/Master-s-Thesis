import pandas as pd


def process_cennik_wrm(json_data):
    records = json_data.get("result", {}).get("records", []) #Jeśli "result" nie istnieje w json_data, zamiast rzucać błąd zwraca pusty słownik {} (to jest domyślna wartość)

    if not records:
        print("Brak danych w odpowiedzi JSON.")
        return None

    df = pd.DataFrame(records)
    return df
def process_lokalizacja_pojazdow_wroc(json_data):
    records = json_data.get("result", {}).get("records", [])

    if not records:
        print("Brak danych w odpowiedzi JSON.")
        return None
    df=pd.DataFrame(records)
    return df

