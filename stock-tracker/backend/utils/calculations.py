def calculate_profit_loss(purchase_price, current_price, quantity):
    """
    Calculate the profit or loss based on purchase price, current price, and quantity of stocks.
    
    :param purchase_price: The price at which the stock was purchased.
    :param current_price: The current market price of the stock.
    :param quantity: The number of shares owned.
    :return: A tuple containing profit/loss amount and profit/loss percentage.
    """
    total_investment = purchase_price * quantity
    current_value = current_price * quantity
    profit_loss_amount = current_value - total_investment
    profit_loss_percentage = (profit_loss_amount / total_investment) * 100 if total_investment != 0 else 0
    
    return profit_loss_amount, profit_loss_percentage

def calculate_total_investment(portfolio):
    """
    Calculate the total investment in the portfolio.
    
    :param portfolio: A list of dictionaries containing stock data with purchase price and quantity.
    :return: Total investment amount.
    """
    total_investment = sum(stock['purchase_price'] * stock['quantity'] for stock in portfolio)
    return total_investment

def calculate_portfolio_value(portfolio, current_prices):
    """
    Calculate the total current value of the portfolio based on current market prices.
    
    :param portfolio: A list of dictionaries containing stock data with quantity.
    :param current_prices: A dictionary mapping stock symbols to their current market prices.
    :return: Total current value of the portfolio.
    """
    total_value = sum(stock['quantity'] * current_prices.get(stock['symbol'], 0) for stock in portfolio)
    return total_value