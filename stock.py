import util
import random
class Stock:
    def __init__(self, name, initial_price, initial_stock, is_new=False):
        self.name = name
        self.price = initial_price 
        self.ideal_price = 0
        self.initial_stock = initial_stock
        self.history = {}   # {date: session_deal}
        self.session_deal = [] # [{"price", "amount"}]

    def gen_financial_report(self, index):
        if self.name == "A":
            return util.FINANCIAL_REPORT_A[index]
        elif self.name == "B":
            return util.FINANCIAL_REPORT_B[index]

    def add_session_deal(self, price_and_amount):
        self.session_deal.append(price_and_amount)

    def update_price(self, date):

     # If trades happened, use the last traded price
     if len(self.session_deal) > 0:
        self.price = self.session_deal[-1]["price"]
        self.history[date] = self.session_deal
        self.session_deal.clear()

     else:
        # If no trades, simulate market fluctuation
        change = random.uniform(-0.03, 0.03)  # ±3% change
        new_price = self.price * (1 + change)

        # prevent negative or zero price
        if new_price < 1:
            new_price = 1

        self.price = new_price

    def get_price(self):
        return self.price


