FROM python:3.8.8


COPY . /test/consumer

WORKDIR /test/consumer

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "KafkaConsumer.py" ]