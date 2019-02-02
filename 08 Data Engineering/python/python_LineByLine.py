# t2.nano, 165Gb volume

import os
import time
import boto3

s3     = boto3.resource('s3')
bucket = s3.Bucket('amazon-reviews-pds')

for obj in bucket.objects.all():
  if obj.key[:3] == 'tsv' and len(obj.key) > 4:
    cmd = 'aws s3 cp s3://amazon-reviews-pds/' + obj.key + ' /home/ec2-user/'
    os.system(cmd)

cmd = 'gunzip /home/ec2-user/*.gz'
os.system(cmd)

start = time.time()

def line_manipulation(line_to_manipulate):

  line_to_manipulate = 'prefix: ' + line_to_manipulate

  return line_to_manipulate

line_count    = 0
file_count    = 0
file_number   = "%05d" % file_count
file_to_write = open('/home/ec2-user/text_' + file_number + '.txt', 'a')

for root, dirs, files in os.walk('/home/ec2-user/'):

  for filename in files:

    if filename[-3:] == 'tsv':

      file_to_read = open('/home/ec2-user/' + filename, 'r')
      line_to_read = file_to_read.readline()

      while line_to_read:

        while line_count < 100000:

          file_to_write.write(line_manipulation(line_to_read))
          line_count  += 1
          line_to_read = file_to_read.readline()

        if line_to_read:

        while line_count < 100000:

          file_to_write.write(line_manipulation(line_to_read))
          line_count  += 1
          line_to_read = file_to_read.readline()

        if line_to_read:

          line_count    = 0
          file_count   += 1
          file_number   = "%05d" % file_count
          file_to_write.close()
          file_to_write = open('/home/ec2-user/text_' + file_number + '.txt', 'a')

      file_to_write.close()
      file_to_read.close()

end = time.time()
print(end - start)/60
