import schedule
import time

def create_stocks(symbols: List[str]) -> List[Stock]:
    return [Stock(symbol) for symbol in symbols]


def track_stocks(stocks: List[Stock]) -> None:
    for stock in stocks:
        stock.get_price()
        stock.notify_observers()


if __name__ == "__main__":
    symbols: List[str] = ['AAPL', 'GOOGL', 'MSFT']
    stocks: List[Stock] = create_stocks(symbols)
    for stock in stocks:
        stock.add_observer(PriceDropObserver(0.05))  # 5% threshold
    schedule.every(10).minutes.do(track_stocks, stocks=stocks)
    while True:
        schedule.run_pending()
        time.sleep(1)