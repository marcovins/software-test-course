from .base import StandardDiscountStrategy, CompositeDiscountStrategy


class UnderageStudentDiscountStrategy(StandardDiscountStrategy):
    def __init__(self):
        super().__init__(discount_rate=0.05)


class UnderageWorkerDiscountStrategy(StandardDiscountStrategy):
    def __init__(self):
        super().__init__(discount_rate=0.03)


class UnderageWorkerStudentDiscountStrategy(CompositeDiscountStrategy):
    def __init__(self):
        super().__init__([UnderageStudentDiscountStrategy(), UnderageWorkerDiscountStrategy()])