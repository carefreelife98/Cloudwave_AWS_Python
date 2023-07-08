import boto3

client = boto3.client('ec2')
instance_tags = client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['csm-boto-?'],
        }
    ]
)
ids = [
    instance['InstanceId']
    for reservation in instance_tags['Reservations']
    for instance in reservation['Instances']
    ]

print(ids)

instance = ids[0]
print(instance)

for i in ids:
    if i == instance:
        print(f'삭제 대상 instance ID : {instance}')
        break