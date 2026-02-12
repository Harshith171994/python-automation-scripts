#!/usr/bin/env python3

import boto3

def list_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    print("S3 Buckets:")
    for bucket in response.get('Buckets', []):
        print(f" - {bucket['Name']}")

def list_ec2_instances(region='us-east-1'):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances()

    print("\nEC2 Instances:")
    for reservation in response.get('Reservations', []):
        for instance in reservation.get('Instances', []):
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            instance_type = instance['InstanceType']
            print(f" - {instance_id} | {instance_type} | {state}")

def main():
    list_s3_buckets()
    list_ec2_instances()

if __name__ == "__main__":
    main()
