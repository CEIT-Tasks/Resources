class DiscountCalculator:
    def apply_discount(self, price, discount_percent=10):
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount