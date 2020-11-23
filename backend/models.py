from mongoengine import *
from extensions import db

class User(db.Document):
    userId = db.StringField(unique=True, required=True)
    employeeType = db.StringField()
    

class Product(db.Document):
    tags = db.ListField(StringField())
    productName = db.StringField()
    productInventory = db.IntField()
    productNumber = db.IntField(required=True)

class Location(db.Document):
    siteName = db.StringField()
    companyName = db.StringField()
    address = db.StringField()


class Order(db.Document):
    orderedBy = db.ReferenceField(User)
    acceptedBy = db.ReferenceField(User)
    products = db.ListField(ReferenceField(Product))
    deliveryLocation = db.ReferenceField(Location)
    productLocation = db.ReferenceField(Location)
    timeOfOrder= db.DateTimeField()