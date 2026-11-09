from .base import StandardDiscountStrategy, CompositeDiscountStrategy


class AdultStudentDiscountStrategy(StandardDiscountStrategy):
    def __init__(self):
        super().__init__(discount_rate=0.0)


class AdultWorkerDiscountStrategy(StandardDiscountStrategy):
    def __init__(self):
        super().__init__(discount_rate=0.15)


class AdultWorkerStudentDiscountStrategy(CompositeDiscountStrategy):
    def __init__(self):
        super().__init__([AdultStudentDiscountStrategy(), AdultWorkerDiscountStrategy()])