import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_right(self):
        assert self.calc.multiply(self, 33, 10) == 330

    def test_division_calculate_right(self):
        assert self.calc.division(self, 300, 100) == 3

    def test_subtraction_calculate_right(self):
        assert self.calc.subtraction(self, 300, 100) == 200

    def test_adding_calculate_right(self):
        assert self.calc.adding(self, 400, 0) == 400