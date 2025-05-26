import pandas as pd

zapelnienie_parkingow_48h= pd.read_csv('Wroclaw_datasets/Zapełnienie_parkingów_48h.csv', parse_dates=['Czas_Rejestracji'])

zapelnienie_parkingow_biezace = pd.read_csv('Wroclaw_datasets/zapelnienie_parkingow_biezace.csv')

zapelnienie_parkingow_48h=pd.DataFrame(zapelnienie_parkingow_48h)
zapelnienie_parkingow_biezace = pd.DataFrame(zapelnienie_parkingow_biezace)
zapelnienie_parkingow_48h['Czas_Rejestracji']=pd.to_datetime(zapelnienie_parkingow_48h['Czas_Rejestracji'], format='mixed', errors='coerce')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print(zapelnienie_parkingow_48h.dtypes)
print("Najstarsza data: ",zapelnienie_parkingow_48h['Czas_Rejestracji'].min(),"Najnowsza data: ", zapelnienie_parkingow_48h['Czas_Rejestracji'].max())
print("Rekordy z brakiem daty: ",zapelnienie_parkingow_48h[zapelnienie_parkingow_48h['Czas_Rejestracji'].isna()])
print("Liczba rekordów z brakiem daty: ",zapelnienie_parkingow_48h['Czas_Rejestracji'].isna().sum())
print("Wiersze z jakimkolwiek brakiem: ",zapelnienie_parkingow_48h[zapelnienie_parkingow_48h.isnull().any(axis=1)])


print(zapelnienie_parkingow_48h.sort_values(['Nazwa', 'Czas_Rejestracji']))
#print(zapelnienie_parkingow_48h, zapelnienie_parkingow_biezace)