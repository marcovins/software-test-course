class StandardDiscountStrategy:
    def __init__(self, discount_rate: float):
        self.discount_rate = discount_rate

    def apply_discount(self, price: float) -> float:
        return price * (1 - self.discount_rate)


class CompositeDiscountStrategy(StandardDiscountStrategy):
    def __init__(self, strategies: list[StandardDiscountStrategy]):
        self.strategies = list(strategies)
        super().__init__(sum(strategy.discount_rate for strategy in self.strategies))


class CompositeDDiscountStrategy(CompositeDiscountStrategy):
    def __init__(self, strategies: list[StandardDiscountStrategy]):
        super().__init__(strategies)

    