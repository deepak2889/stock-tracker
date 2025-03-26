from flask import Blueprint, request, jsonify
from models.portfolio import Portfolio

portfolio_bp = Blueprint('portfolio', __name__)
portfolio = Portfolio()

@portfolio_bp.route('/portfolio', methods=['GET'])
def get_portfolio():
    return jsonify(portfolio.get_portfolio_data()), 200

@portfolio_bp.route('/portfolio/add', methods=['POST'])
def add_stock():
    data = request.json
    symbol = data.get('symbol')
    quantity = data.get('quantity')
    purchase_price = data.get('purchase_price')
    
    if not symbol or not quantity or not purchase_price:
        return jsonify({"error": "Missing data"}), 400
    
    portfolio.add_stock(symbol, quantity, purchase_price)
    return jsonify({"message": "Stock added successfully"}), 201

@portfolio_bp.route('/portfolio/profit-loss', methods=['GET'])
def calculate_profit_loss():
    return jsonify(portfolio.calculate_profit_loss()), 200