from .base import StandardDiscountStrategy, CompositeDiscountStrategy, CompositeDDiscountStrategy
from .underage_strategies import UnderageStudentDiscountStrategy, UnderageWorkerDiscountStrategy, UnderageWorkerStudentDiscountStrategy
from .adult_strategies import AdultStudentDiscountStrategy, AdultWorkerDiscountStrategy, AdultWorkerStudentDiscountStrategy
from .old_strategies import OldDiscountStrategy

__all__ = [
    "StandardDiscountStrategy",
    "CompositeDiscountStrategy",
    "CompositeDDiscountStrategy",
    "UnderageStudentDiscountStrategy",
    "UnderageWorkerDiscountStrategy",
    "UnderageWorkerStudentDiscountStrategy",
    "AdultStudentDiscountStrategy",
    "AdultWorkerDiscountStrategy",
    "AdultWorkerStudentDiscountStrategy",
    "OldDiscountStrategy"
]