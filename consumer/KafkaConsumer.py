import json
from pathlib import Path
from mongoengine import connect
from kafka import KafkaConsumer
from pydantic import BaseModel
import sys
sys.path.append('C:\SCM\backend\app')
import models

base_dir = Path(__file__).resolve().parent


# connect(db="SCM", host="localhost", port=27017)
connect(db="SCM", host="mongodb+srv://admin:F24850346c!@cluster0.r9xezko.mongodb.net/?retryWrites=true&w=majority")
# bootstrap_servers = "backend-kafka-1:9092"
# bootstrap_servers = 'localhost:9092'
bootstrap_servers = "root-kafka-1:9092"
topicName = 'transport_data'

class TransportData(BaseModel):
        Battery_Level: int
        Device_Id: int
        First_Sensor_temperature: int
        Route_From: str
        Route_To: str

try:
    consumer = KafkaConsumer(topicName,bootstrap_servers = bootstrap_servers,auto_offset_reset = 'earliest')
    for data in consumer:
        data = json.loads(data.value)
        Transport_Data = models.Transport_data(
            Battery_Level = data['Battery_Level'],
            Device_Id = data['Device_Id'],
            First_Sensor_temperature = data['First_Sensor_temperature'],
            Route_From = data['Route_From'],
            Route_To = data['Route_To']                        
        )
        
        Transport_Data.save() 
        print(Transport_Data)
except KeyboardInterrupt:
    sys.exit()