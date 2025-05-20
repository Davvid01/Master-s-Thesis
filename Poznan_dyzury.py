import requests

# URL API
url = "https://bip.poznan.pl/api-json/bip/dyzury-radnych/"

try:
    # Wysłanie żądania GET do API
    response = requests.get(url)
    response.raise_for_status()  # Sprawdzenie statusu odpowiedzi

    # # Parsowanie odpowiedzi JSON
    # data = response.json()
    #
    # # Bezpieczne pobranie danych o dyżurach
    # dyzury = []
    # if isinstance(data.get("data"), list) and len(data["data"]) > 0:
    #     dyzury = data["data"][0].get("dyzury", {}).get("items", [])
    #
    # # Wypisanie dyżurów lub informacji, że nie ma danych
    if dyzury:
        for dyzur in dyzury:
            print(dyzur)
    else:
        print("Brak dostępnych dyżurów w danych API.")

except requests.exceptions.RequestException as e:
    print(f"Błąd podczas komunikacji z API: {e}")
except ValueError as e:
    print(f"Błąd parsowania JSON: {e}")
except Exception as e:
    print(f"Nieoczekiwany błąd: {e}")
