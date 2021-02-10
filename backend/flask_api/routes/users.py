import json
import logging as logger
from flask import Blueprint, jsonify, request
from flask import current_app as app
from flask_api.extensions import db
from flask_api.models import User

logger.basicConfig(level=logger.DEBUG)

users = Blueprint(
    'users', __name__,
)

@users.route('/users/', methods=['POST'])
def create_user():
    try:
        body = request.get_json()
        user = User(**body).save()
        id = user.id
        logger.debug("created user: ", user.name)
        return {'id': str(id)}, 201
    except Exception as e:
        logger.warning("Encountered exception: ", e)
        return "Error", 400

@users.route('/users/', methods=['DELETE'])
def delete_user():
    try:
        body = request.get_json()
        name = body["name"]
        user = User.objects.get(name=name)
        user.delete()
        logger.debug("deleted user: ", user.name)
        return "Done", 201 
    except Exception as e:
        logger.warning("Encountered Exception: ", e)
        return "Error", 400

@users.route('/users/', methods=['GET'])
def view_users():
    userList= User.objects.all().values_list('name')
    logger.debug(userList)
    return "Done", 201