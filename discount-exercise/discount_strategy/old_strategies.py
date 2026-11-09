from .base import StandardDiscountStrategy


class OldDiscountStrategy(StandardDiscountStrategy):
    def __init__(self):
        super().__init__(discount_rate=0.10)