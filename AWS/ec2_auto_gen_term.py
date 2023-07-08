import boto3

# seoul region에 있는 모든 instance를 가져올 수 있게된다.

# ImageId:ami-0ea4d4b8dc1e46212
# InstanceType:t2.micro
# KeyName:csm-keypair
# MaxCount:
# MinCount:
# SecurityGroupIds:sg-0efc600c5c7d205a4
# SubnetId:subnet-0b76e94cbb884989c
# name:csm-boto-default-4

def terminate_instances():
    del_num = int(input('삭제할 instance 개수를 입력하세요:'))
    instance_id = input('삭제할 instance의 ID를 입력하세요:')

    if del_num == 0:
        print('중지한 instance가 없습니다.')
        return

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

    for i in ids:
        if i == instance_id:
            print(f'삭제 대상 instance ID : {instance_id}')
            break
    # if instance_id not in ids:
    #     print(f'삭제 대상 instance ID를 찾지 못했습니다 - 종료')
    #     return

    for i in range(del_num):
        print(f'ec2 instance를 중지합니다. id = {instance_id}')
        client.terminate_instances(
            InstanceIds=[
                f'{instance_id}',
            ],
            # DryRun=True|False
        )


def gen_instances():
    run_num = int(input('생성할 instance 개수를 입력하세요:'))
    print('생성할 ec2 instance의 정보 입력 단계')
    ImageId = input('ImageId:')
    InstanceType = input('InstanceType:')
    KeyName = input('KeyName:')
    MaxCount = input('MaxCount:')
    if MaxCount == '':
        MaxCount = 1
    MinCount = input('MinCount:')
    if MinCount == '':
        MinCount = 1
    SecurityGroupIds = input('SecurityGroupIds:')
    SubnetId = input('SubnetId:')
    name = input('name:')
    if run_num == 0:
        print('생성한 instance가 없습니다.')
        return
    int(MaxCount)
    int(MinCount)
    client = boto3.client('ec2')

    for i in range(1, run_num+1):
        print(f'ec2 instance{i}를 생성합니다.')
        print(
            f'ImageId={ImageId},InstanceType={InstanceType},KeyName={KeyName},MaxCount={MaxCount},MinCount={MinCount},SecurityGroupIds={[SecurityGroupIds]},SubnetId={SubnetId}')
        client.run_instances(
            ImageId=ImageId,
            InstanceType=InstanceType,
            KeyName=KeyName,
            MaxCount=MaxCount,
            MinCount=MinCount,
            SecurityGroupIds=[SecurityGroupIds],
            SubnetId=SubnetId,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': name
                        },
                    ]
                },
            ]
        )
    print('AWS ec2 instance 생성 완료.')

    print('instance 정보를 보시겠습니까? [y/n]')
    confirm = input()
    if confirm == 'y':
        print(f'ImageId={ImageId},InstanceType={InstanceType},KeyName={KeyName},MaxCount={MaxCount},MinCount={MinCount},SecurityGroupIds={[SecurityGroupIds]},SubnetId={SubnetId}')

if __name__ == '__main__':

    print('AWS ec2 instance 생성 및 삭제를 진행합니다.')
    # gen_instances()

    terminate_instances()
