import boto3
from  boto3.dynamodb.conditions import Key,Attr
def read_table(start_date,end_date):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table_name = 'WildfiresTable'
    table = dynamodb.Table(table_name)
    response = table.scan(

    FilterExpression=Key('date').between(start_date,end_date)
    
)
    return response