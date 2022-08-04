import random

"""
Задачи на математические операции.
"""

# возможные операции
operator = ["+", "-", "*", ":"]


def get_expressions():
    operations = get_random_operations()


def get_random_operations():
    """Возвращает рандомное количество рандомных арифметических операций"""
    count = random.randint(1, 4)
    operations = list()
    for _ in range(count):
        operations.append(random.choice(operator))
    return operations


def test():
    get_expressions()


