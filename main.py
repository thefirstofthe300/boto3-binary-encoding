import json
import boto3
import logging

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('boto3').setLevel(logging.DEBUG)
logging.getLogger('botocore').setLevel(logging.DEBUG)

dynamodb = boto3.client('dynamodb', region_name="us-west-1")

with open("record.json") as f:
    item = json.load(f)

logging.info(f"item={item}")

target_ddb_name = "binary-serialization"

logging.info(f"target_ddb_name={target_ddb_name}; item={item}")
response = dynamodb.put_item(
    TableName=target_ddb_name, Item=item)
