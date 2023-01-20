import socket
import json
import time
import random
s = socket.socket()


countries = [
    "Chicago, United States",
    "Kabul, Afghanistan",   
    "Sydney, Australia",
    "Manama, Bahrain",
    "Dhaka, Bangladesh",    
    "Ottawa, Canada",    
    "Beijing, China",    
    "Paris, France",
    "Berlin, Germany",
    "Hong kong, Hong Kong",
    "Chennai, India",
    "Netanya, Israel",
    "Tokyo, Japan",
    "Katmandu, Nepal",
    "London, United Kingdom",
]

random_country1 = random.choice(countries)
random_country2 = random.choice(countries)
random_country3 = random.choice(countries)
random_country4 = random.choice(countries)

print("Socket Created")
s.bind(('',12345))
s.listen(3)
print("waiting for connections")
c, addr = s.accept()
data =[{
"Battery_Level":random.uniform(1,10),
 "Device_Id":random.randint(10000000,99999999),
 "First_Sensor_temperature":random.uniform(1,99) ,
 "Route_From":str(random_country1),
 "Route_To":str(random_country2),
 },{
"Battery_Level":random.uniform(1,10),
 "Device_Id":random.randint(10000000,99999999),
 "First_Sensor_temperature":random.uniform(1,99) ,
 "Route_From":str(random_country3),
 "Route_To":str(random_country4),
 }
       
]
while True:
    try:
        print("connected with", addr)
        userdata = (json.dumps(data)+"\n").encode('utf-8')
        print(userdata)
        c.send(userdata)
        time.sleep(100)
    except Exception as e:
        print(e)
        c.close()