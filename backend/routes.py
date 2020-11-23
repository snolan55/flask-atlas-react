import json
import logging as logger
from flask import Blueprint, jsonify, request
from flask import current_app as app
from extensions import db
from models import *

logger.basicConfig(level=logger.DEBUG)

routes_bp = Blueprint(
    'routes_bp', __name__,
)

@routes_bp.route('/', methods=['POST'])
def create_user():
    try:
        record = json.loads(request.data)
        user = User(userId=record['userId'],
                    employeeType=record['employeeType'])
        user.save()
        logger.debug("user: ", user.userId)
        return "Done", 201
    except Exception as e:
        logger.warning("Encountered exception: ", e)
        return "Error", 400

@routes_bp.route('/')
def view_users():
    logger.debug(User.objects.all().values_list('userId'))
    return "Done", 201