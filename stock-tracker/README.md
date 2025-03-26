# Stock Tracker

This project is a stock tracking application that integrates with the National Stock Exchange (NSE) and Bombay Stock Exchange (BSE) APIs to provide users with stock search capabilities, portfolio management, and profit/loss calculations.

## Features

- **Stock Search**: Users can search for stocks by symbol or name and retrieve detailed stock information.
- **Portfolio Management**: Users can create and manage their stock portfolios, adding stocks and tracking their investments.
- **Profit/Loss Calculations**: The application calculates profit and loss based on the purchase price and current market price of stocks.

## Technologies Used

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **APIs**: NSE and BSE stock data APIs

## Project Structure

```
stock-tracker
├── backend
│   ├── app.py
│   ├── models
│   │   └── portfolio.py
│   ├── routes
│   │   ├── stocks.py
│   │   └── portfolio.py
│   ├── services
│   │   ├── nse_api.py
│   │   └── bse_api.py
│   ├── utils
│   │   └── calculations.py
│   └── templates
│       └── index.html
├── frontend
│   ├── css
│   │   └── styles.css
│   ├── js
│   │   └── scripts.js
│   └── index.html
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd stock-tracker
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```
   python backend/app.py
   ```

4. Open your browser and navigate to `http://localhost:5000` to access the application.

## Usage

- Use the stock search feature to find stocks by entering their symbol or name.
- Manage your portfolio by adding stocks and viewing your total investment.
- Check the profit/loss for your investments based on current market prices.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.