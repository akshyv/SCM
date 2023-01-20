FROM python:3.8.8

COPY . /test/producer

WORKDIR /test/producer

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "KafkaProducer.py" ]