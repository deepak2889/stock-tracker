from flask import Flask
from routes.stocks import stock_routes
from routes.portfolio import portfolio_routes

app = Flask(__name__)

# Configuration settings can be added here
app.config['SECRET_KEY'] = 'your_secret_key'

# Registering routes
app.register_blueprint(stock_routes)
app.register_blueprint(portfolio_routes)

if __name__ == '__main__':
    app.run(debug=True)