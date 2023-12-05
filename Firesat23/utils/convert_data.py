import boto3
from decimal import Decimal

from utils.get_continent import get_continent

# DynamoDB resource and table name are constants, so we can initialize them once
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table_name = 'WildfiresTable'

def generate_row_database(row: dict) -> dict:
    """
    Generate a dictionary representing a row in the database.
    """
    return {
        "continent_date": f"{row['continent']}_{row['date'][:14]}",  # Continent in two characters + date in ISO 8601 format cut to the hour
        "id": f"{row['date']}+{round(float(row['x']), 2)}+{round(float(row['y']), 2)}",  # ISO 8601 + latitude + longitude with two-digit approximation
        "conf": row['conf'],  # Confidence of detection
        "sat": "noaa-goes16",
        "x": Decimal(row['x']),
        "y": Decimal(row['y'])
    }

def row_to_dict(row: list, header: list) -> dict:
    """
    Convert a row of data into a dictionary using the header for keys.
    """
    a_dict = dict(zip(header, row))
    a_dict['continent'] = get_continent(a_dict['x'], a_dict['y'])
    return a_dict

def insert_batch(items: list) -> None:
    """
    Insert a batch of items into the DynamoDB table.
    """
    table = dynamodb.Table(table_name)
    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item)

def read_table() -> dict:
    """
    Read the entire DynamoDB table.
    """
    table = dynamodb.Table(table_name)
    return table.scan()['Items']