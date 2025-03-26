import requests

BSE_API_URL = "https://api.bseindia.com/BseIndiaAPI/api/StockReach/StockReach.aspx"

def fetch_stock_data(stock_symbol):
    params = {
        'scripcode': stock_symbol,
        'type': 'equity'
    }
    response = requests.get(BSE_API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def search_stock_by_name(stock_name):
    params = {
        'search': stock_name
    }
    response = requests.get(BSE_API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None