import pandas as pd
from decimal import Decimal

from utils.get_continent import get_continent
#function that recieve an array of strings and returns an array of arrays
def convert_data(data):
    new_data = []
    for d in data:
        new_data.append(d.split(','))
    return new_data

def convert_dataframe(array, date):
    df=pd.DataFrame(array[1:],columns=array[0])
    df['x']=pd.to_numeric(df['x'])
    df['y']=pd.to_numeric(df['y'])
    df['date']=pd.to_datetime(df['date'])
    df['continent']=df.apply(lambda row: get_continent(row['x'], row['y']), axis=1)
    return df[df['date']>=date]


def generate_row_database(row: dict)->list:
    return {
    "continent_date": "{}_{}".format(row['continent'],row['date'][:14]), # Es el continente en dos caracteres + fecha con formato ISO 8601 cortada hasta la hora
    "id": "{}+{}+{}".format(row['date'],round(float(row['x']),2),round(float(row['y']),2)), # Es el ISO 8601 + latitud + longitud con aproximación de dos dígitos
    "conf": 15, # Es la confianza de la detección
    "sat": "noaa-goes16",
    "x": Decimal(row['x']),
    "y": Decimal(row['y'])
  }

def row_to_dict(row:list,header:list)->dict:
    a_dict={}
    for i in range(len(row)):
        a_dict[header[i]]=row[i]
    a_dict['continent']=get_continent(a_dict['x'], a_dict['y'])
    return(a_dict)