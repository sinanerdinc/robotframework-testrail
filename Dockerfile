FROM python:3.12.0a6-alpine3.17
MAINTAINER Sinan Erdinc <mail@sinanerdinc.com>
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python", "robot_testrail.py"]