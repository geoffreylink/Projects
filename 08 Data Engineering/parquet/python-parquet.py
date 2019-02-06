# aws s3 cp s3://amazon-reviews-pds/tsv/amazon_reviews_us_Wireless_v1_00.tsv.gz .

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

df    = pd.read_csv('amazon_reviews_us_Wireless_v1_00.tsv', sep='\t', error_bad_lines=False, dtype={'marketplace': str,'customer_id': str,'review_id': str,'product_id': str,'product_parent': str,'product_title': str,'product_category': str,'star_rating': str,'helpful_votes': str,'total_votes': str,'vine': str,'verified_purchase': str,'review_headline': str,'review_date': str,'review_body': str})

table = pa.Table.from_pandas(df)

#pq.write_table(table, 'amazon_reviews_us_Wireless_v1_00.parquet', compression='gzip')

pq.write_to_dataset(table, '/home/ec2-user/', partition_cols=['product_category','review_date'], compression='gzip')
