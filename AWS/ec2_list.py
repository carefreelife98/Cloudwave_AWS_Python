import boto3
import csv

# YOUR_REGION = 'ap-northeast-2'

# Create an EC2 client
ec2 = boto3.client('ec2')

# Retrieve all instances (both running and stopped)
instances = ec2.describe_instances()

# Create a list to hold the instance details
instance_details = []

# Append the details of each instance to the list
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        name = ''
        if 'Tags' in instance:
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    name = tag['Value']
                    break
        else:
            name = 'none'
        private_ip_address = instance.get('PrivateIpAddress', '')
        public_ip_address = instance.get('PublicIpAddress', '')
        instance_details.append({'Name': name, 'Instance ID': instance_id, 'Private IP': private_ip_address, 'Public IP': public_ip_address})

# Write the instance details to a CSV file
with open('instance_details.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Instance ID', 'Private IP', 'Public IP'])
    writer.writeheader()
    for instance in instance_details:
        writer.writerow(instance)
