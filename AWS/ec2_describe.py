import boto3

# seoul region에 있는 모든 instance를 가져올 수 있게된다.
client = boto3.client('ec2')

instance_tags = client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['csm-svr-py'],
        }
    ]
)

ids = [
    instance['InstanceId']
    for reservation in instance_tags['Reservations']
    for instance in reservation['Instances']
       ]

print(f'instance 를 삭제합니다 : id = {ids[0]}')

response = client.terminate_instances(
    InstanceIds=[
        f'{ids[0]}',
    ],
    # DryRun=True|False
)
