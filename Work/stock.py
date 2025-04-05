class Stock:
    def __init__(self, name: str, shares: int, price: float):
        # Any value stored on `self` is instance data
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, share_count: int):
        self.shares -= share_count
