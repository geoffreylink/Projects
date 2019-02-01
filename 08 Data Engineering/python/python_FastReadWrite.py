import os
import boto3

s3     = boto3.resource('s3')
bucket = s3.Bucket('amazon-reviews-pds')

for obj in bucket.objects.all():
  if obj.key[:3] == 'tsv' and len(obj.key) > 4:
    cmd = 'aws s3 cp s3://amazon-reviews-pds/' + obj.key + ' /home/ec2-user/'
    os.system(cmd)

cmd = 'gunzip /home/ec2-user/*.gz'
os.system(cmd)
