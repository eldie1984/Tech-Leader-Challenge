import boto3
from decimal import Decimal

from utils.get_continent import get_continent


def generate_row_database(row: dict)->list:
    return {
    "continent_date": "{}_{}".format(row['continent'],row['date'][:14]), # Es el continente en dos caracteres + fecha con formato ISO 8601 cortada hasta la hora
    "id": "{}+{}+{}".format(row['date'],round(float(row['x']),2),round(float(row['y']),2)), # Es el ISO 8601 + latitud + longitud con aproximación de dos dígitos
    "conf": row['conf'], # Es la confianza de la detección
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

def insert_batch(items:list) -> None:

  dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
  table_name = 'WildfiresTable'

  table = dynamodb.Table(table_name)
  with table.batch_writer() as batch:
    for item in items:
        batch.put_item(Item=item)

def read_table():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table_name = 'WildfiresTable'
    table = dynamodb.Table(table_name)
    response = table.scan()
    items = response['Items']

    for item in items:
        print(item)
    return items