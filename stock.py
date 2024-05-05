import yfinance as yf

class Stock:
    def __init__(self, symbol: str):
        self.symbol: str = symbol
        self.current_price: float = 0.0
        self.previous_price: float = 0.0
        self.observers: List["PriceDropObserver"] = []

    def get_price(self) -> None:
        stock_data = yf.Ticker(self.symbol)
        self.previous_price = self.current_price
        self.current_price = stock_data.history(period='1d')['Close'][-1]

    def add_observer(self, observer: "PriceDropObserver") -> None:
        self.observers.append(observer)

    def notify_observers(self) -> None:
        for observer in self.observers:
            observer.update(self.symbol, self.current_price, self.previous_price)

