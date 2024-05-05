class PriceDropObserver:
    def __init__(self, threshold: float):
        self.threshold: float = threshold

    def update(self, symbol: str, current_price: float, previous_price: float) -> None:
        price_change = current_price - previous_price
        if price_change < 0 and abs(price_change) >= (self.threshold * previous_price):
            print(f"Price drop detected for {symbol}! Sending email...")
            EmailSender.send_email(symbol, current_price, previous_price)
