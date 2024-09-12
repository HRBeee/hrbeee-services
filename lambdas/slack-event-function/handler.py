import boto3
import json

sqs = boto3.client('sqs')
QUEUE_URL = os.environ.get('SLACK_EVENT_QUEUE_URL')

def lambda_handler(event, context):
    slack_event = {
        "event": {
            "type": "message",
            "text": "What is our PTO policy?",
            "user": "U12345678"
        }
    }

    message = slack_event['event']['text']
    user_id = slack_event['event']['user']

    sqs_message = {
        'message': message,
        'user_id': user_id
    }
    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(sqs_message)
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Message sent to SQS')
    }
