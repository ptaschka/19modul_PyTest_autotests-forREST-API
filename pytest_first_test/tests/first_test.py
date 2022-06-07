import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multyply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_correct(self):
        assert self.calc.division(self, 50, 10) == 5

    def test_subtraction_calculate_correct(self):
        assert self.calc.subtraction(self, 13, 7) == 6

    def test_added_calculate_correct(self):
        assert self.calc.adding(self, 6, 1) == 7

