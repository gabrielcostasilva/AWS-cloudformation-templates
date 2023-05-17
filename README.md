# CloudFormation Templates
This repo groups templates for using with [AWS CloudFormation](https://aws.amazon.com/cloudformation/). CloudFormation is a service for provisioning resources that implements the concept of [infrastructure as code - IaC](https://aws.amazon.com/devops/what-is-devops/?nc1=f_cc#iac). Therefore, a given infrastructure can be created and deleted automatically.

Each folder holds a set of examples. Hopefully, folder names are self-explanatory ;)

- [`email-message`](./email-message/) creates a SNS topic and an email subscription using a [CloudFormation template](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SNS.html), and sends a message using a Python app with the [`Boto3` library](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html).

- [`loan-request`](https://github.com/gabrielcostasilva/cloud-loan-request.git) is a project that integrates Step Functions, SNS and DynamoDB. **Note that** this project is in another repository. 
