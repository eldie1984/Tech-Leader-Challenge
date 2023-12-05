import boto3
import csv
from datetime import datetime
from moto import mock_dynamodb

# Local module imports
from database.init import init_db
from api.firesat23 import get_wildfires_last_24_hours
from utils.convert_data import generate_row_database,row_to_dict,insert_batch,read_table

# Decorator to mock DynamoDB
@mock_dynamodb
def lambda_handler (event: dict, context: dict) -> dict:
  # Initialize the database
  init_db()

  # Get the wildfire data for the last 24 hours
  firesat_csv: str = get_wildfires_last_24_hours()

  # Convert the upload date from a string to a datetime object
  uploadFrom = datetime.strptime(event["uploadFrom"], "%Y-%m-%dT%H:%M:%S+00:00")

  # Split the data into lines
  lines = firesat_csv.splitlines()

  # The first line contains the headers
  header = lines[0].split(',')

  # Generate the items for the database
  items = [generate_row_database(row_to_dict(row.split(','), header)) for row in lines[1:] if row_to_dict(row.split(','), header)['continent'] != 'UNKNOWN' and datetime.strptime(row_to_dict(row.split(','), header)['date'], "%Y-%m-%dT%H:%M:%S+00:00") > uploadFrom]

  # Insert the items into the database
  insert_batch(items)

  # Read the entire database
  wholeDatabase: dict = read_table()

  # Return the status and the database data
  return { "statusCode": 200, "body": wholeDatabase}