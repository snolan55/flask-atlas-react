from mongoengine import *

class Product(Document)
    tags = ListField(StringField(max_length=50))