import os
import sys
import boto3
import pandas as pd

s3     = boto3.resource('s3')
bucket = s3.Bucket('amazon-reviews-pds')

for obj in bucket.objects.all():
  if obj.key[:3] == 'tsv' and len(obj.key) > 4:
    cmd = 'aws s3 cp s3://amazon-reviews-pds/' + obj.key + ' /home/ec2-user/'
    print cmd
    os.system(cmd)

#s3.Object('pywren1', 'amazon_reviews_us_Wireless_v1_00.tsv').upload_file(Filename='amazon_reviews_us_Wireless_v1_00.tsv')
#s3.Object('pywren1', 'amazon_reviews_us_Wireless_v1_00.tsv').download_file('/home/ec2-user/homer.txt')

def line_manipulation(line_to_manipulate):

  line_to_manipulate = 'prefix: ' + line_to_manipulate + '\n'

  return line_to_manipulate

obj        = s3.Object('pywren1', 'amazon_reviews_us_Wireless_v1_00.tsv')
body       = obj.get()['Body']
blocksize  = 1024*1024
buf        = body.read(blocksize)
build_file = ''
file_count = 0
line_count = 0

while len(buf) > 0:

  lines = buf.split('\n')

  for line in lines:

    if line.count('\t') > 13:

      if line_count < 100000:

        line_count += 1
        build_file = build_file + line_manipulation(line)

      else:

        file_number   = "%05d" % file_count
        file_to_write = open('/home/ec2-user/text_' + file_number + '.txt', 'a')
        file_to_write.write(build_file)
        file_to_write.close()
        build_file  = ''
        line_count  = 0
        file_count += 1

  if line.count('\t') > 13:
    buf = body.read(blocksize)
  else:
    buf = line + body.read(blocksize)

if line_count > 0:
  file_number   = "%05d" % file_count
  file_to_write = open('/home/ec2-user/text_' + file_number + '.txt', 'a')
  file_to_write.write(build_file)
  file_to_write.close()
