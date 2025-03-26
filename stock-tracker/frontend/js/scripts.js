// This file contains JavaScript code for handling user interactions on the frontend, such as searching for stocks and updating the portfolio.

document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('search-form');
    const stockResults = document.getElementById('stock-results');
    const portfolioForm = document.getElementById('portfolio-form');
    const portfolioList = document.getElementById('portfolio-list');

    searchForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const searchInput = document.getElementById('search-input').value;
        fetchStockData(searchInput);
    });

    portfolioForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const stockSymbol = document.getElementById('portfolio-stock-symbol').value;
        const stockQuantity = document.getElementById('portfolio-stock-quantity').value;
        addToPortfolio(stockSymbol, stockQuantity);
    });

    function fetchStockData(query) {
        fetch(`/api/stocks/search?query=${query}`)
            .then(response => response.json())
            .then(data => {
                displayStockResults(data);
            })
            .catch(error => console.error('Error fetching stock data:', error));
    }

    function displayStockResults(data) {
        stockResults.innerHTML = '';
        data.forEach(stock => {
            const stockItem = document.createElement('div');
            stockItem.className = 'stock-item';
            stockItem.innerHTML = `
                <h3>${stock.name} (${stock.symbol})</h3>
                <p>Current Price: ₹${stock.currentPrice}</p>
            `;
            stockResults.appendChild(stockItem);
        });
    }

    function addToPortfolio(symbol, quantity) {
        fetch('/api/portfolio/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ symbol, quantity })
        })
        .then(response => response.json())
        .then(data => {
            updatePortfolioList(data);
        })
        .catch(error => console.error('Error adding to portfolio:', error));
    }

    function updatePortfolioList(data) {
        portfolioList.innerHTML = '';
        data.forEach(stock => {
            const portfolioItem = document.createElement('li');
            portfolioItem.textContent = `${stock.symbol}: ${stock.quantity}`;
            portfolioList.appendChild(portfolioItem);
        });
    }
});