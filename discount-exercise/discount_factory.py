from discount_strategy import (
    AdultStudentDiscountStrategy,
    AdultWorkerDiscountStrategy,
    AdultWorkerStudentDiscountStrategy,
    OldDiscountStrategy,
    StandardDiscountStrategy,
    UnderageStudentDiscountStrategy,
    UnderageWorkerDiscountStrategy,
    UnderageWorkerStudentDiscountStrategy,
)


class DiscountFactory:
    @staticmethod
    def get_discount_strategy(age, is_student, is_worker):
        if age < 18:
            return DiscountFactory._build_underage_strategy(is_student, is_worker)
        if age <= 60:
            return DiscountFactory._build_adult_strategy(is_student, is_worker)
        return OldDiscountStrategy()

    @staticmethod
    def _build_underage_strategy(is_student, is_worker):
        if is_student and is_worker:
            return UnderageWorkerStudentDiscountStrategy()
        if is_student:
            return UnderageStudentDiscountStrategy()
        if is_worker:
            return UnderageWorkerDiscountStrategy()
        return StandardDiscountStrategy(0.0)

    @staticmethod
    def _build_adult_strategy(is_student, is_worker):
        if is_student and is_worker:
            return AdultWorkerStudentDiscountStrategy()
        if is_student:
            return AdultStudentDiscountStrategy()
        if is_worker:
            return AdultWorkerDiscountStrategy()
        return StandardDiscountStrategy(0.0)
