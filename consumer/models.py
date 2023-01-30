from mongoengine import Document, StringField, IntField, DateField, DynamicDocument

    
class User(Document):
    username = StringField(max_length=100)
    password = StringField()
    
class Shipments(Document):
    user_name = StringField()
    Invoice_no = IntField()
    container_no = IntField()
    shipment_description = StringField()
    route_details = StringField()
    goods_type = StringField()
    device = StringField()
    expected_delivery_date = DateField()
    PO_number = StringField()
    delivery_no = IntField()
    NDC_no = IntField()
    batch_id = IntField()
    Serial_no_of_goods = IntField()
    
    
class DeviceData(DynamicDocument):
    Battery_Level = IntField()
    Device_Id = IntField()
    First_Sensor_temperature = IntField()
    Route_From = StringField()
    Route_To = StringField()    