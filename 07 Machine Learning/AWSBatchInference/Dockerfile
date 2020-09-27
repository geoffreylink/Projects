FROM amazonlinux:latest
RUN yum -y update
RUN yum -y install python-pip
RUN pip install boto3
ADD inference_coach.py /usr/local/bin/inference_coach.py
ENTRYPOINT ["/usr/local/bin/inference_coach.py"]
