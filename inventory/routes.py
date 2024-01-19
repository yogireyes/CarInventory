from flask import Blueprint

inventory = Blueprint('inventory', __name__)


@inventory.route('/cars')
def cars():
    return 'Car Inventory'
