from flask import Blueprint, request, jsonify

shipment_bp = Blueprint('shipment', __name__)

@shipment_bp.route('/track', methods=['GET'])
def track_shipment():
    return jsonify({"message": "Shipment tracking data"})
