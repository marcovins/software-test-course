from discount_factory import DiscountFactory

class Client:
    def __init__(self, name, age, is_student=False, is_worker=False):
        self.name = name
        self.age = age
        self._is_student = is_student
        self._is_worker = is_worker
        self._set_discount_strategy()

    def _set_discount_strategy(self):
        self.discount_strategy = DiscountFactory.get_discount_strategy(self.age, self._is_student, self._is_worker)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def is_student(self):
        return self._is_student

    def is_worker(self):
        return self._is_worker
