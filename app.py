import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # Specify the EC2 instance parameters
    instance_params = {
        'ImageId': 'ami-0c55b159',  # Example AMI ID (Amazon Linux 2)
        'InstanceType': 't2.micro',  # Instance type
        'MinCount': 2,  # Minimum number of instances to launch
        'MaxCount': 2,  # Maximum number of instances to launch
        'KeyName': 'my-key',  # Specify your EC2 key pair name
        'SecurityGroupIds': ['sg-xxxxxxxx'],  # Security group ID
        'SubnetId': 'subnet-xxxxxxxx',
