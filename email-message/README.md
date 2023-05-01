# E-MAIL NOTIFICATION


1. Create SNS Topic and subscription
```
aws cloudformation create-stack \      
--stack-name sns-publish-app-messages \
--template-body file://cf-topic-template.yaml
```

Response example 

```
{
    "StackId": "arn:aws:cloudformation:us-east-1:<YOUR-ACCOUNT-HERE>:stack/sns-publish-app-messages/83dd5c00-d965-11ed-9fe9-120ce60f3577"
}
```

2. Check the creation process
```
aws cloudformation describe-stacks \   
--stack-name sns-publish-app-messages
```

Response example
```
{
    "Stacks": [
        {
            "StackId": "arn:aws:cloudformation:us-east-1:<YOUR-ACCOUNT-HERE>:stack/sns-publish-app-messages/0097f8b0-d964-11ed-ae55-0a1f2df645cb",
            "StackName": "sns-publish-app-messages",
            "CreationTime": "2023-04-12T18:58:24.967000+00:00",
            "DeletionTime": "2023-04-12T19:02:10.027000+00:00",
            "RollbackConfiguration": {},
            "StackStatus": "DELETE_IN_PROGRESS",
            "DisableRollback": false,
            "NotificationARNs": [],
            "Tags": [],
            "EnableTerminationProtection": false,
            "DriftInformation": {
                "StackDriftStatus": "NOT_CHECKED"
            }
        }
    ]
}
```

3. Checkout your email to confirming your subscription

4. Figure out the SNS topic ARN

```
aws cloudformation describe-stack-resources \
--stack-name sns-publish-app-messages
```

Response example
```
{
    "StackResources": [
        {
            "StackName": "sns-publish-app-messages",
            "StackId": "arn:aws:cloudformation:us-east-1:<YOUR-ACCOUNT-HERE>:stack/sns-publish-app-messages/83dd5c00-d965-11ed-9fe9-120ce60f3577",
            "LogicalResourceId": "PublishAppMessages",
            "PhysicalResourceId": "arn:aws:sns:us-east-1:<YOUR-ACCOUNT-HERE>:PublishInfoMessagesToUsers",
            "ResourceType": "AWS::SNS::Topic",
            "Timestamp": "2023-04-12T19:09:26.748000+00:00",
            "ResourceStatus": "CREATE_COMPLETE",
            "DriftInformation": {
                "StackResourceDriftStatus": "NOT_CHECKED"
            }
        }
    ]
}
```

5. Update the `publish-message.py` code with the topic ARN

6. Install the `Boto3` library
```
python -m pip install boto3
```

7. Run `publish-message.py` to publishing the message
```
python publish-message.py
```

8. Checkout your e-mail for the published message

9. Delete your CloudFormation stack
```
aws cloudformation delete-stack \
--stack-name sns-publish-app-messages
```
