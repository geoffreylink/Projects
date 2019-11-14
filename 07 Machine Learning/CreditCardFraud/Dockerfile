FROM amazonlinux:latest
RUN yum -y install which unzip aws-cli
RUN yum install -y python python-dev python-pip
RUN pip install sagemaker
ADD fetch_and_run.sh /usr/local/bin/fetch_and_run.sh
WORKDIR /tmp
USER nobody
ENTRYPOINT ["/usr/local/bin/fetch_and_run.sh"]
