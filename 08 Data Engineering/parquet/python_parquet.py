# m5.4xlarge, 125Gb gp2 volume

import os
import boto3
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

s3     = boto3.resource('s3')
bucket = s3.Bucket('amazon-reviews-pds')

for obj in bucket.objects.all():

  if obj.key[:3] == 'tsv' and len(obj.key) > 4:

    cmd = 'aws s3 cp s3://amazon-reviews-pds/' + obj.key + ' /home/ec2-user/'
    os.system(cmd)

cmd = 'gunzip /home/ec2-user/*.gz'
os.system(cmd)

for root, dirs, files in os.walk('/home/ec2-user/'):

  for filename in files:

    if filename[-3:] == 'tsv':

      df    = pd.read_csv(filename, sep='\t', error_bad_lines=False, dtype={'marketplace': str,'customer_id': str,'review_id': str,'product_id': str,'product_parent': str,'product_title': str,'product_category': str,'star_rating': str,'helpful_votes': str,'total_votes': str,'vine': str,'verified_purchase': str,'review_headline': str,'review_date': str,'review_body': str})

      table = pa.Table.from_pandas(df)

      pq.write_to_dataset(table, '/home/ec2-user/', partition_cols=['product_category','review_date'], compression='gzip')
