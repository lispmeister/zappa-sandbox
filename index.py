import json
import datetime


def handler(event, context):
    data = {
        'output': 'Hello World',
        'timestamp1': datetime.datetime.utcnow().isoformat(),
        'timestamp2': datetime.datetime.utcnow().isoformat(),
        'timestamp3': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
