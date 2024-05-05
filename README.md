# Stock Trader App

## Introduction
Stock Trader is a Python application for tracking stock prices and detecting price drops in real-time. It allows users to monitor their favorite stocks and receive email alerts when the price drops by a certain percentage.

## Features
- Fetches real-time stock prices from Yahoo Finance API.
- Monitors price changes every 10 minutes and sends email alerts for price drops.
- Supports tracking stocks from American (NYSE, NASDAQ) and Canadian (TSX) markets.
- Easily configurable to track any list of stocks and set custom thresholds for price drops.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/stock-trader.git```

2. Install the required dependencies:
    
    ```pip install -r requirements.txt```

3. Usage
    Open the config.py file and customize the list of stocks to track (STOCKS) and the threshold for price drops (PRICE_DROP_THRESHOLD).

4. Run the application:
    ```python main.py```


4. Configuration
    STOCKS: List of stock symbols to track (e.g., ['AAPL', 'GOOGL', 'MSFT']).
    PRICE_DROP_THRESHOLD: Threshold for price drops (e.g., 0.05 for 5% drop).

5. Contributing
    Contributions are welcome! If you have any ideas, suggestions, or bug fixes, feel free to open an issue or submit a pull request.

