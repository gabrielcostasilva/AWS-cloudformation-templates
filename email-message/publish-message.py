import boto3

client = boto3.client('sns')

response = client.publish(
    TopicArn="arn:aws:sns:us-east-1:<YOUR-ACCOUNT-HERE>:PublishInfoMessagesToUsers", 
    Message="Hello World!")