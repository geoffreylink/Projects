#!/usr/bin/python

import os
import boto3

count=1
while count < 2:
  filename = f'{count:07d}'+'.txt'
  f=open(filename,'w+')
  f.close()
  boto3.client('s3').upload_file(filename, 'project1-landing', filename)
  os.remove(filename)
  count+=1
