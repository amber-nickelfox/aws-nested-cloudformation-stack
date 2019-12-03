import json

# import requests


def handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world from admin",
        }),
    }
