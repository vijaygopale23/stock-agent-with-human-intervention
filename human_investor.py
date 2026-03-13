class HumanInvestor:

    def __init__(self, cash):
        self.cash = cash
        self.stock_a = 0
        self.stock_b = 0

    def buy(self, stock, amount, price):
        cost = amount * price

        if self.cash >= cost:
            self.cash -= cost

            if stock == "A":
                self.stock_a += amount
            else:
                self.stock_b += amount

            print(f"✅ Bought {amount} shares of {stock} at {price}")

        else:
            print("❌ Not enough cash")

    def sell(self, stock, amount, price):

        if stock == "A" and self.stock_a >= amount:
            self.stock_a -= amount
            self.cash += amount * price

        elif stock == "B" and self.stock_b >= amount:
            self.stock_b -= amount
            self.cash += amount * price

        else:
            print("❌ Not enough shares")
            return

        print(f"💰 Sold {amount} shares of {stock} at {price}")

    def show_portfolio(self, price_a, price_b):

        value = (
            self.cash
            + self.stock_a * price_a
            + self.stock_b * price_b
        )

        print("\n📊 YOUR PORTFOLIO")
        print("Cash:", self.cash)
        print("Stock A:", self.stock_a)
        print("Stock B:", self.stock_b)
        print("Total Value:", value)