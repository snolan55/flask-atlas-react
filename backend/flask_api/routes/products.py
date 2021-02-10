import json
import logging as logger
from flask import Blueprint, jsonify, request
from flask import current_app as app
from flask_api.extensions import db
from flask_api.models import Product
from mongoengine.queryset.visitor import Q

logger.basicConfig(level=logger.DEBUG)

products = Blueprint(
    'products', __name__,
)

@products.route('/products/', methods=['POST'])
def create_product():
    try:
        body = request.get_json()
        products = Product(**body).save()
        logger.debug("created product: ", products.number)
        product = jsonify(products)
        return product, 201
    except Exception as e:
        logger.warning("Encountered exception: ", e)
        return "Error", 400

@products.route('/products/', methods=['DELETE'])
def delete_product():
    try:
        body = request.get_json()
        number = body["number"]
        products = Product.objects.get(number=number)
        products.delete()
        logger.debug("deleted products: ", products.number)
        return "Done", 201 
    except Exception as e:
        logger.warning("Encountered Exception: ", e)
        return "Error", 400

@products.route('/products/', methods=['GET'])
def view_products():
    query = request.args.get('query')
    logger.debug(query)
    if query:
        productList = Product.objects(Q(name__contains=query) | Q(tags__contains=query))
        productList = jsonify(productList)
        logger.debug(productList)
        return productList, 201
    else:
        productList= Product.objects
        productList= jsonify(productList)
        logger.debug(productList)
        return productList, 201