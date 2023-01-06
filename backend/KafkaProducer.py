import socket    
import json 
from kafka import KafkaProducer
import json

socket_connection = socket.socket() 
HOST = "127.0.0.1"
# HOST = "socket"
PORT = 12345               
socket_connection.connect((HOST,PORT))
bootstrap_servers = 'localhost:9092'
# bootstrap_servers = "kafka"
topicName = 'transport_data'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers, retries = 5,value_serializer=lambda m: json.dumps(m).encode('utf-8'))

while True:
    try:
        data=socket_connection.recv(70240).decode()
        json_acceptable_string = data.replace("'", "\"")
        load_data = json.loads(json_acceptable_string)
        print(load_data)
        for data in load_data:
            producer.send(topicName,data)
            print(data)
    except Exception as exception:
        print(exception)
socket_connection.close()