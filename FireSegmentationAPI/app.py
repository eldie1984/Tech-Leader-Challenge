import boto3
import json
from moto import mock_dynamodb

from database.init import init_db
from database.mockData import insert_mock_data
from segmentation.segmentation import segmentacionDeIncendios
from utils.db_operations import read_table

@mock_dynamodb
def lambda_handler (event: dict, context: dict) -> dict:

  init_db()
  insert_mock_data()

  jsonParams = json.loads(event["body"])
  datos=read_table(jsonParams['fromDate'],jsonParams['toDate'])
  fuegos: list[dict] = [
    {"id": "0", "x": 0.0, "y": 0.0, "time":"2023-01-01T00:00"},
    {"id": "1", "x": 1.0, "y": 0.0, "time":"2023-01-01T00:00"},
    {"id": "2", "x": 0.0, "y": 1.0, "time":"2023-01-01T00:00"},
    {"id": "3", "x": 10.0, "y": 10.0, "time":"2023-01-01T00:00"},
    {"id": "4", "x": 10.0, "y": 11.0, "time":"2023-01-01T00:00"}
  ]
  num, lista =segmentacionDeIncendios(datos['Items'])
  return { "statusCode": 200, "body": {"num": num,"lista":lista}}