FROM apache/airflow:slim-2.3.3-python3.8

USER root

RUN apt-get update && \
    apt-get install -y libmysqlclient-dev gcc libkrb5-dev

USER airflow

COPY requirements.txt /usr/local/airflow/requirements.txt

RUN pip install -r /usr/local/airflow/requirements.txt
