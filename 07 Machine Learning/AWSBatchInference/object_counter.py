#!/usr/bin/python

import boto3

count=0
for objectsummary in boto3.resource('s3').Bucket('project1-processed').objects.all():
  count+=1
print(count)
