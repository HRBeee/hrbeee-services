import json
import os

def lambda_handler(event, context):
    # Simulated incoming Slack event
    slack_event = {
        "event": {
            "type": "message",
            "text": "What is our PTO policy?",
            "user": "U12345678"
        }
    }

    # Extract message and user_id from the simulated event
    message = slack_event['event']['text']
    user_id = slack_event['event']['user']

    # Prepare a response (or perform another action)
    response_message = {
        'message': message,
        'user_id': user_id
    }

    # Print the response message (for debugging purposes)
    print(json.dumps(response_message))

    # Return a response indicating that the processing is complete
    return {
        'statusCode': 200,
        'body': json.dumps('Message processed successfully')
    }
