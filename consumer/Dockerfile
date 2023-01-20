FROM python:3.8.8

RUN pip install kafka-python

COPY . /test/consumer

WORKDIR /test/consumer

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "KafkaConsumer.py" ]