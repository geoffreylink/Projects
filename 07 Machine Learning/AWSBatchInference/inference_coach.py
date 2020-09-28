#!/usr/bin/python

#Cloud9
#sudo pip install --user --upgrade awscli
#sudo pip install boto3
#chmod 764  

#https://github.com/awslabs/amazon-sagemaker-examples/blob/master/introduction_to_applying_machine_learning/xgboost_direct_marketing/xgboost_direct_marketing_sagemaker.ipynb
#Use ml.c5.large for endpoint (allows for autoscaling, t-series do not allow for autoscaling due to bursting)
#https://aws.amazon.com/blogs/compute/creating-a-simple-fetch-and-run-aws-batch-job/

#Schedule CloudWatch Event for every 15 minutes (CloudWatch submits jobs without verifying existing execution)
#Cron expression: 0,15,30,45 * * * ? *
#10 minutes to spin-up coach instance + 10 minutes to spin-up endpoint up + 10 minutes to spin-up runner spot instances = massive parallelism

#Use AWS Aurora Postgres Serverless Database (Postgres = AUTOCOMMIT)
#CREATE TABLE IS_SCRIPT_RUNNING(YES_OR_NO CHAR(1));
#INSERT INTO IS_SCRIPT_RUNNING (YES_OR_NO) VALUES ('N');
#CREATE SEQUENCE PROJECT1;
#CREATE TABLE PREDICTIONS(SEQUENCE INT PRIMARY KEY, FILE VARCHAR, PREDICTION FLOAT);

import time
import boto3

bucket_landing = 'project1-landing'
endpoint_name  = 'project1-endpoint'

resourceArn = 'arn:aws:rds:us-east-1:888888888888:cluster:project-1'
secretArn   = 'arn:aws:secretsmanager:us-east-1:888888888888:secret:rds-db-credentials/cluster-888888888888/postgres-888888'

rds_client   = boto3.client('rds-data'               , region_name='us-east-1')
pred_client  = boto3.client('sagemaker'              , region_name='us-east-1')
batch_client = boto3.client('batch'                  , region_name='us-east-1')
scale_client = boto3.client('application-autoscaling', region_name='us-east-1')

count_of_objects = 0
for objectsummary in boto3.resource('s3').Bucket(bucket_landing).objects.all():
  count_of_objects+=1

is_script_running = rds_client.execute_statement(resourceArn=resourceArn,secretArn=secretArn,
                                                 sql = 'select YES_OR_NO from IS_SCRIPT_RUNNING')['records'][0][0]['stringValue']

if is_script_running == 'N' and count_of_objects > 0:

  rds_client.execute_statement(resourceArn=resourceArn,secretArn=secretArn,
                               sql        = 'UPDATE IS_SCRIPT_RUNNING SET YES_OR_NO = :Y_or_N',
                               parameters = [{'name':'Y_or_N', 'value':{'stringValue': 'Y'}}])

  pred_client.create_endpoint(EndpointName       = endpoint_name,
                              EndpointConfigName = 'xgboost-2020-09-19-14-55-26-095')

  while pred_client.describe_endpoint(EndpointName=endpoint_name)['EndpointStatus']=='Creating':
    time.sleep(60)

  scale_client.register_scalable_target(ServiceNamespace  = 'sagemaker',
                                        ResourceId        = 'endpoint/project1-endpoint/variant/AllTraffic',
                                        ScalableDimension = 'sagemaker:variant:DesiredInstanceCount',
                                        MinCapacity       = 1,
                                        MaxCapacity       = 3)

  scale_client.put_scaling_policy(PolicyName                               = 'inference_runner',
                                  ServiceNamespace                         = 'sagemaker',
                                  ResourceId                               = 'endpoint/project1-endpoint/variant/AllTraffic',
                                  ScalableDimension                        = 'sagemaker:variant:DesiredInstanceCount',
                                  PolicyType                               = 'TargetTrackingScaling',
                                  TargetTrackingScalingPolicyConfiguration = {'TargetValue'                   : 3,
                                                                              'PredefinedMetricSpecification' : {'PredefinedMetricType':'SageMakerVariantInvocationsPerInstance'}})

  for objectsummary in boto3.resource('s3').Bucket(bucket_landing).objects.all():
    batch_client.submit_job(jobName            = bucket_landing+'-'+objectsummary.key.replace('.','-'),
                            jobDefinition      = 'inference_runner',
                            jobQueue           = 'inference_runner',
                            containerOverrides = {'environment': [{'name': 'FILE', 'value':objectsummary.key}]})

  while batch_client.list_jobs(jobQueue='inference_runner',jobStatus='SUBMITTED')['jobSummaryList'] or \
        batch_client.list_jobs(jobQueue='inference_runner',jobStatus='PENDING')['jobSummaryList']   or \
        batch_client.list_jobs(jobQueue='inference_runner',jobStatus='RUNNABLE')['jobSummaryList']  or \
        batch_client.list_jobs(jobQueue='inference_runner',jobStatus='STARTING')['jobSummaryList']  or \
        batch_client.list_jobs(jobQueue='inference_runner',jobStatus='RUNNING')['jobSummaryList']:
    time.sleep(60)

  pred_client.delete_endpoint(EndpointName=endpoint_name)
  rds_client.execute_statement(resourceArn=resourceArn,secretArn=secretArn,
                               sql        = 'UPDATE IS_SCRIPT_RUNNING SET YES_OR_NO = :Y_or_N',
                               parameters = [{'name':'Y_or_N', 'value':{'stringValue': 'N'}}])
