#!/usr/bin/env python3
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
response = s3.list_buckets()

for bucket in response['Buckets']:
  try:
    encryption = s3.get_bucket_encryption(Bucket=bucket['Name'])
    rules = encryption['ServerSideEncryptionConfiguration']['Rules']
    print('Bucket: %s, Encryption: %s' % (bucket['Name'], rules))
  except ClientError as e:
    if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
      print('Bucket: %s, no server-side encryption' % (bucket['Name']))