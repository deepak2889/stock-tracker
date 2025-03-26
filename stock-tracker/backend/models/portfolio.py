class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity, purchase_price):
        if symbol in self.stocks:
            self.stocks[symbol]['quantity'] += quantity
            self.stocks[symbol]['purchase_price'] = purchase_price
        else:
            self.stocks[symbol] = {'quantity': quantity, 'purchase_price': purchase_price}

    def get_portfolio(self):
        return self.stocks

    def total_investment(self):
        total = 0
        for stock in self.stocks.values():
            total += stock['quantity'] * stock['purchase_price']
        return total

    def calculate_profit_loss(self, current_prices):
        profit_loss = {}
        for symbol, data in self.stocks.items():
            if symbol in current_prices:
                current_value = current_prices[symbol] * data['quantity']
                investment = data['quantity'] * data['purchase_price']
                profit_loss[symbol] = current_value - investment
        return profit_loss