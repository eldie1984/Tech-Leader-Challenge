import boto3
import csv
from datetime import datetime
from moto import mock_dynamodb

from database.init import init_db
from api.firesat23 import get_wildfires_last_24_hours

from utils.convert_data import generate_row_database,row_to_dict,insert_batch,read_table

@mock_dynamodb
def lambda_handler (event: dict, context: dict) -> dict:

  init_db()
  firesat_csv: str = get_wildfires_last_24_hours()
  uploadFrom = datetime.strptime(event["uploadFrom"], "%Y-%m-%dT%H:%M:%S+00:00")
  firstLine: bool = True
  items=[]

  for row in firesat_csv.splitlines():
    # Extraer la información, detectar continente y subir a la base de datos
    # Se recomienda usar la función "get_continent" del archivo "utils/get_continent.py"
    # Modularizar la solucion para hacerla más clara y entendible
    if firstLine:
        header=row.split(',')
        firstLine = False
    else:
        row_dic=row_to_dict(row.split(','),header)
        if row_dic['continent']!='UNKNOWN' and datetime.strptime(row_dic['date'], "%Y-%m-%dT%H:%M:%S+00:00")>uploadFrom:
            items.append(generate_row_database(row_dic))
  insert_batch(items)
  # Escribir el codigo para leer toda la base de datos y outputearla.
  # Esto sera util para testear el codigo
  wholeDatabase: dict = read_table()
  return { "statusCode": 200, "body": wholeDatabase}


