import boto3
from boto3.dynamodb.conditions import Key

# DynamoDB resource and table name are constants, so we can initialize them once
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table_name = 'WildfiresTable'

def read_table(start_date: str, end_date: str) -> dict:
    """
    This function reads data from the DynamoDB table between the specified start and end dates.
    It returns the response from the table scan as a dictionary.
    """
    table = dynamodb.Table(table_name)
    response = table.scan(FilterExpression=Key('date').between(start_date, end_date))
    return response