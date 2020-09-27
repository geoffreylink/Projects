#!/usr/bin/python

import boto3

for objectsummary in boto3.resource('s3').Bucket('project1-processed').objects.all():
  boto3.resource('s3').Object('project1-processed', objectsummary.key).delete()
