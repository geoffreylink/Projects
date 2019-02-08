# t2.micro, 100Gb gp2 volume

import os
import sys
import boto3

s3     = boto3.resource('s3')
bucket = s3.Bucket('amazon-reviews-pds')

for obj in bucket.objects.all():
  if obj.key[:3] == 'tsv' and len(obj.key) > 4:
    cmd = 'aws s3 cp s3://amazon-reviews-pds/' + obj.key + ' /home/ec2-user/'
#    os.system(cmd)

cmd = 'gunzip /home/ec2-user/*.gz'
#os.system(cmd)

for root, dirs, files in os.walk('/home/ec2-user/'):
  for filename in files:
    if filename[-3:] == 'tsv':
      continue
#      s3.Object('pywren1', filename).upload_file(Filename=filename)

def line_manipulation(line_to_manipulate):

  line_to_manipulate = 'prefix: ' + line_to_manipulate + '\n'

  return line_to_manipulate

bucket     = s3.Bucket('pywren1')
build_file = ''
file_count = 0
line_count = 0

for obj in bucket.objects.all():

  print obj.key

  obj       = s3.Object('pywren1', obj.key)
  body      = obj.get()['Body']
  blocksize = 1024*1024
  buf       = body.read(blocksize)

  while len(buf) > 0:

    lines = buf.split('\n')

    for line in lines:

      if line.count('\t') > 13:

        if line_count < 99999:

          line_count   += 1
          build_file    = build_file + line_manipulation(line)

        else:

          build_file    = build_file + line_manipulation(line)
          file_number   = "%05d" % file_count
          file_to_write = open('/home/ec2-user/text_' + file_number + '.txt', 'a')
          file_to_write.write(build_file)
          file_to_write.close()
          build_file    = ''
          line_count    = 0
          file_count   += 1

    buf = line + body.read(blocksize)

  if line_count > 0:
    file_number   = "%05d" % file_count
    file_to_write = open('/home/ec2-user/text_' + file_number + '.txt', 'a')
    file_to_write.write(build_file)
    file_to_write.close()
    build_file    = ''
    line_count    = 0
    file_count   += 1

