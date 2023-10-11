import pytest
from raise_function import Employee as E

@pytest.fixture
def employee():
    """Employee instance which will be available to all functions."""
    employee = E('Aayush', 'Rai', 5000000)
    return employee

def test_give_default_raise(employee):
    """Does the function work while giving default raise?"""
    give_raise = employee.give_raise()
    employee.display_raised_salary()

def test_give_custom_raise(employee):
    """Does the function work while giving custom raise?"""
    give_raise = employee.give_raise(3000000)
    employee.display_raised_salary()