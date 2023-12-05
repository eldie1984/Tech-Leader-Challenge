import boto3
import json
from moto import mock_dynamodb

# Local module imports
from database.init import init_db
from database.mockData import insert_mock_data
from segmentation.segmentation import segmentacionDeIncendios
from utils.db_operations import read_table

# Decorator to mock DynamoDB
@mock_dynamodb
def lambda_handler (event: dict, context: dict) -> dict:
    """
    This function is the entry point for the AWS Lambda function.
    It initializes the database, inserts mock data, reads data from the database,
    segments the data, and returns the number of segments and the list of segments.
    """
    # Initialize the database and insert mock data
    init_db()
    insert_mock_data()

    # Parse the JSON parameters from the event body
    jsonParams = json.loads(event["body"])

    # Read data from the database between the specified dates
    datos = read_table(jsonParams['fromDate'], jsonParams['toDate'])

    # Segment the data
    num, lista = segmentacionDeIncendios(datos['Items'])

    # Return the status code, number of segments, and list of segments
    return { "statusCode": 200, "body": {"num": num, "lista": lista} }