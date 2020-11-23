import json
from flask import Blueprint, jsonify, request
from flask import current_app as app
from extensions import db
from models import *

routes_bp = Blueprint(
    'routes_bp', __name__,
)

@routes_bp.route('/', methods=['POST'])
def create_user():
    record = json.loads(request.data)
    user = User(userId=record['userId'],
                employeeType=record['employeeType'])
    user.save()
    return "Done", 201

@routes_bp.route('/')
def view_users():
    print(User.objects.all().values_list('userId'))
    return "Done", 201