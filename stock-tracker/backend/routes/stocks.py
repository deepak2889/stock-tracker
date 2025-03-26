from flask import Blueprint, request, jsonify
from backend.services.nse_api import fetch_nse_stock_data
from backend.services.bse_api import fetch_bse_stock_data

stocks_bp = Blueprint('stocks', __name__)

@stocks_bp.route('/search', methods=['GET'])
def search_stock():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400

    nse_data = fetch_nse_stock_data(query)
    bse_data = fetch_bse_stock_data(query)

    return jsonify({
        'nse': nse_data,
        'bse': bse_data
    })