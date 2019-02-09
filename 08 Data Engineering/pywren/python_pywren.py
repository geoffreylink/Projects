# t2.micro, 40Gb gp2 volume

import os
import sys
import time
import boto3
import pywren

pywren_bucket = 'pywren1'
client        = boto3.client('s3')
s3            = boto3.resource('s3')

def split_tsv_file(tsv_filename):

  client = boto3.client('s3')
  s3     = boto3.resource('s3')

  def line_manipulation(line_to_manipulate):

    line_to_manipulate = 'prefix: ' + line_to_manipulate + '\n'

    return line_to_manipulate

  build_file = ''
  file_count = 0
  line_count = 0
  obj        = s3.Object(pywren_bucket, tsv_filename)
  body       = obj.get()['Body']
  blocksize  = 1024*1024
  buf        = body.read(blocksize)

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
          client.put_object(Body=build_file, Bucket=pywren_bucket, Key=obj.key + '_' + file_number)
          build_file    = ''
          line_count    = 0
          file_count   += 1

    if line.count('\t') < 14:
      buf = line + body.read(blocksize)
    else:
      buf = body.read(blocksize)

  if line_count > 0:
    file_number   = "%05d" % file_count
    client.put_object(Body=build_file, Bucket=pywren_bucket, Key=obj.key + '_' + file_number)
    build_file    = ''
    line_count    = 0
    file_count   += 1

  return tsv_filename

if __name__ == '__main__':

  for obj in s3.Bucket('amazon-reviews-pds').objects.all():
    if obj.key[:3] == 'tsv' and len(obj.key) > 4 and obj.size / 1024 / 1024 / 1024 < 1:
      cmd = 'aws s3 cp s3://amazon-reviews-pds/' + obj.key + ' /home/ec2-user/'
      print cmd
      os.system(cmd)

  cmd = 'gunzip /home/ec2-user/*.gz'
  print cmd
  os.system(cmd)

  for root, dirs, files in os.walk('/home/ec2-user/'):
    for filename in files:
      if filename[-3:] == 'tsv':
        print filename
        s3.Object(pywren_bucket, filename).upload_file(Filename=filename)

  files_to_split = []
  for obj in s3.Bucket(pywren_bucket).objects.all():
    files_to_split.append(obj.key)
  print files_to_split

  start = time.time()

  wrenexec = pywren.default_executor()
  futures  = wrenexec.map(split_tsv_file, files_to_split)
  print pywren.get_all_results(futures)

  end = time.time()
  print(end - start)/60
