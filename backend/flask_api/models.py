from mongoengine import *
from .extensions import db

class User(db.Document):
    name = db.StringField(unique=True, required=True)
    role = db.StringField()
    

class Product(db.Document):
    img = db.StringField()
    tags = db.ListField(StringField())
    name = db.StringField()
    number = db.StringField(unique=True, required=True)

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