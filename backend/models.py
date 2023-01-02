from mongoengine import Document, StringField, IntField, DateField

class Employee(Document):
    name = StringField(max_length=100)
    email = StringField()
    emp_id = IntField()
    
class User(Document):
    username = StringField(max_length=100)
    password = StringField()
    
class Shipments(Document):
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
    
    
    