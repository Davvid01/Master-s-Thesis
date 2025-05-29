import pandas as pd

zapelnienie_parkingow_48h= pd.read_csv('Wroclaw_datasets/Zapełnienie_parkingów_48h.csv', parse_dates=['Czas_Rejestracji'])

zapelnienie_parkingow_biezace = pd.read_csv('Wroclaw_datasets/zapelnienie_parkingow_biezace.csv')

zapelnienie_parkingow_48h=pd.DataFrame(zapelnienie_parkingow_48h)
zapelnienie_parkingow_biezace = pd.DataFrame(zapelnienie_parkingow_biezace)
zapelnienie_parkingow_48h['Czas_Rejestracji']=pd.to_datetime(zapelnienie_parkingow_48h['Czas_Rejestracji'], format='mixed', errors='coerce')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

def data_check(data):
    #data['Czas_Rejestracji'] = pd.to_datetime(data['Czas_Rejestracji'], format='mixed', errors='coerce')
    print(data.dtypes)
    print("Najstarsza data: ",data['Czas_Rejestracji'].min(),"Najnowsza data: ", data['Czas_Rejestracji'].max())
    print("Rekordy z brakiem daty: ",data[zapelnienie_parkingow_48h['Czas_Rejestracji'].isna()])
    print("Liczba rekordów z brakiem daty: ",data['Czas_Rejestracji'].isna().sum())
    print("Wiersze z jakimkolwiek brakiem: ",data[data.isnull().any(axis=1)])
    print("W kolejności 'Nazwa',;'Czas_Rejestracji': ", data.sort_values(['Nazwa','Czas_Rejestracji']))


print(data_check(zapelnienie_parkingow_48h))
print(data_check(zapelnienie_parkingow_biezace))
#print(zapelnienie_parkingow_48h.sort_values(['Nazwa', 'Czas_Rejestracji']))