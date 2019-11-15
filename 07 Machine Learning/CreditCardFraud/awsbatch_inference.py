#!/usr/bin/python

# https://aws.amazon.com/blogs/compute/creating-a-simple-fetch-and-run-aws-batch-job/
# aws s3 cp awsbatch_inference.py s3://creditcardfraud123/awsbatch_inference.py
# Job Name:              prediction_test_001
# BATCH_FILE_TYPE        script
# BATCH_FILE_S3_URL:     s3://creditcardfraud123/awsbatch_inference.py
# AWS_DEFAULT_REGION:    us-east-1
# AWS_ACCESS_KEY_ID:     abc123
# AWS_SECRET_ACCESS_KEY: abc123

from sagemaker.model import Model
from sagemaker.predictor import RealTimePredictor
from sagemaker.predictor import csv_serializer
from sagemaker.predictor import json_deserializer
from sagemaker.amazon.amazon_estimator import get_image_uri

endpoint_name = 'creditcardfraudlogistic'

Model(
      model_data = 's3://creditcardfraud123/logistic/output/linear-learner-191112-2119-002-ac3cc459/output/model.tar.gz',
      image      = get_image_uri(
                                 region_name  = 'us-east-1'     ,
                                 repo_name    = 'linear-learner',
                                 repo_version = 'latest'
                                ),
       role       = 'AmazonSageMaker-ExecutionRole-20191005T164168'
     ).deploy(
              initial_instance_count = 1              ,
              instance_type          = 'ml.t2.2xlarge',
              endpoint_name          = endpoint_name
             )

predictor              = RealTimePredictor(endpoint_name)
predictor.content_type = 'text/csv'
predictor.serializer   = csv_serializer
predictor.deserializer = json_deserializer

data = '83916.0,-0.46612620502545604,1.05888696127596,1.6867741713450801,-0.10791713399150099,-0.0534658672545062,-0.67078459643593,0.657296448523877,0.0267747128155009,-0.777065639315537,-0.16451379457928,1.6033857689344901,1.08437897734507,0.621801289885425,0.209210718774203,0.054395914001364995,0.30196805090530604,-0.610384355760504,-0.0111685840197793,0.22161067607904003,0.14522945875429,-0.155193422608588,-0.386047830532794,-0.019162727901044996,0.53588061095157,-0.22766218008636102,0.0387309462886897,0.266651773221212,0.114305983146032,2.58'

print(' ')
if predictor.predict(data)['predictions'][0]['predicted_label'] == 0:
    print('Not a Fraudulent Transaction')
else:
    print('Fraudulent Transaction')

predictor.delete_endpoint()
predictor.delete_model()
