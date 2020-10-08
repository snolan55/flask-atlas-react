from flask import Blueprint
from flask import current_app as app

routes_bp = Blueprint(
    'routes_bp', __name__,
)

@routes_bp.route('/product_input', methods=['POST'])
def product_input():
    product = request.get_json()