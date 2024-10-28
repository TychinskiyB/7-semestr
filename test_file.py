import pytest
from discriminant import calculate_discriminant

def test_positive_discriminant():
 """Тест для случая, когда дискриминант больше нуля."""
 assert calculate_discriminant(1, 5, 6) == 1

def test_zero_discriminant():
 """Тест для случая, когда дискриминант равен нулю."""
 assert calculate_discriminant(1, -2, 1) == 0

def test_negative_discriminant():
 """Тест для случая, когда дискриминант меньше нуля."""
 assert calculate_discriminant(1, 1, 1) == -3
