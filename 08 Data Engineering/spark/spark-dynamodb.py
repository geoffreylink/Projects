### Create DynamoDB Tables and Populate Data via Hive metadata ###

https://aws.amazon.com/blogs/aws/aws-howto-using-amazon-elastic-mapreduce-with-dynamodb/

CREATE EXTERNAL TABLE orders_s3_export ( order_id string, customer_id string, order_date int, total double ) PARTITIONED BY (year string, month string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LOCATION 's3://elastic-mapreduce/samples/ddb-orders';
CREATE EXTERNAL TABLE orders_ddb_2012_01 ( order_id string, customer_id string, order_date bigint, total double ) STORED BY 'org.apache.hadoop.hive.dynamodb.DynamoDBStorageHandler' TBLPROPERTIES ( "dynamodb.table.name" = "Orders-2012-01", "dynamodb.column.mapping" = "order_id:Order ID,customer_id:Customer ID,order_date:Order Date,total:Total");
ALTER TABLE orders_s3_export ADD PARTITION (year='2012', month='01');
INSERT OVERWRITE TABLE orders_ddb_2012_01 SELECT order_id, customer_id, order_date, total FROM orders_s3_export limit 1;
SELECT customer_id, sum(total) spend, count(*) order_count FROM orders_ddb_2012_01 WHERE order_date >= unix_timestamp('2012-01-01', 'yyyy-MM-dd') AND order_date < unix_timestamp('2012-01-08', 'yyyy-MM-dd') GROUP BY customer_id ORDER BY spend desc LIMIT 5;

### Additional jars required for Spark-submit/PySpark call ###

pyspark --jars /usr/share/aws/emr/ddb/lib/emr-ddb-hive.jar,/usr/share/aws/emr/ddb/lib/emr-ddb-hadoop.jar

### HiveQL file entries to create the metadata for PySpark to Access DynamoDB Tables as an initial step in EMR (Auto-terminating job) ###

CREATE EXTERNAL TABLE orders_ddb_2012_01 ( order_id string, customer_id string, order_date bigint, total double ) STORED BY 'org.apache.hadoop.hive.dynamodb.DynamoDBStorageHandler' TBLPROPERTIES ( "dynamodb.table.name" = "Orders-2012-01", "dynamodb.column.mapping" = "order_id:Order ID,customer_id:Customer ID,order_date:Order Date,total:Total");
CREATE EXTERNAL TABLE dest_orders_ddb_2012_01 ( order_id string, customer_id string, order_date bigint, total double ) STORED BY 'org.apache.hadoop.hive.dynamodb.DynamoDBStorageHandler' TBLPROPERTIES ( "dynamodb.table.name" = "dest-Orders-2012-01", "dynamodb.column.mapping" = "order_id:Order ID,customer_id:Customer ID,order_date:Order Date,total:Total");

### PySpark Example ###

from pyspark.sql import SparkSession

spark = SparkSession.builder.enableHiveSupport().getOrCreate()

df = spark.sql("SELECT order_id, customer_id, order_date, total FROM orders_ddb_2012_01");
df.write.mode('append').saveAsTable('dest_orders_ddb_2012_01', format="hive");
