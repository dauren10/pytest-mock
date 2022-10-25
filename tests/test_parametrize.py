import pytest


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9",  54)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


'''Встроенный декоратор pytest.mark.parametrize позволяет параметризовать аргументы тестовых функций. 
Ниже приведен типичный пример тестовой функции, реализующей проверку того, 
что определенный ввод приводит к ожидаемому выводу:
Здесь декоратор @parametrize определяет три различных кортежа (test_input, expected), 
так что функция test_eval будет работать три раза, используя их по очереди:
'''
