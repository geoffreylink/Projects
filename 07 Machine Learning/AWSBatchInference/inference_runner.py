#!/usr/bin/python

# Use spot m4.large instances for AWS Batch for inference_runner and a minimum of 64Mb and 1 vCPU in the Job Definition
# Use a minimum of 2 vCPUs in the Compute Environment
# Use on-demand m4.large instances for AWS Batch for inference_coach
# Use SEPARATE AWS Batch resources for inference_runner and inference_coach

import os
import boto3

bucket_landing   = 'project1-landing'
bucket_processed = 'project1-processed'
endpoint_name    = 'project1-endpoint'

resourceArn = 'arn:aws:rds:us-east-1:888888888888:cluster:project-1'
secretArn   = 'arn:aws:secretsmanager:us-east-1:888888888888:secret:rds-db-credentials/cluster-888888888888/postgres-888'

rds_client  = boto3.client('rds-data',          region_name='us-east-1')
pred_client = boto3.client('sagemaker-runtime', region_name='us-east-1')

sequence    = rds_client.execute_statement(resourceArn=resourceArn,secretArn=secretArn,
                                           sql        = 'SELECT nextval(:PROJECT1)',
                                           parameters = [{'name':'PROJECT1', 'value':{'stringValue': 'PROJECT1'}}]
                                          )['records'][0][0]['longValue']

prediction = float(pred_client.invoke_endpoint(EndpointName = endpoint_name,
                                               Body         = '25,1,999,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0')['Body'].read().decode('utf-8'))

rds_client.execute_statement(resourceArn=resourceArn,secretArn=secretArn,
                             sql        = 'INSERT INTO PREDICTIONS (SEQUENCE, FILE, PREDICTION) VALUES (:sequence, :file, :prediction)',
                             parameters = [{'name':'sequence'  , 'value':{'longValue'  : sequence}},
                                           {'name':'file'      , 'value':{'stringValue': os.environ['FILE']}},
                                           {'name':'prediction', 'value':{'doubleValue': prediction}}])

boto3.resource('s3').Object(bucket_processed, os.environ['FILE']).copy_from(CopySource=bucket_landing+'/'+os.environ['FILE'])
boto3.resource('s3').Object(bucket_landing, os.environ['FILE']).delete()
