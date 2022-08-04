import math
import random

from mat import mat
from .templates import TEMPLATES

"""
Генератор задач на проценты.

Задачи на проценты разделены по категориям:
A - Найти процента от числа.
B - Найти число, зная значение некоторого его процента.
C - Найти сколько число составляет процентов от другого числа.
D - Найти разницу в % между 2 числами.
"""


def get_perc_task_type_a(difficult: str = None) -> tuple:
    """
    Найти процент от числа.
    :param difficult: уровень сложности.
    :return: вопрос, кортеж с ответами, уровень сложности задачи.
    """
    template = get_random_template('A')

    # вычисления
    num = random.randrange(150, 1000, 10)
    perc = random.randrange(10, 90, 10)

    # рендер вопроса
    question = template['question'].format(perc=perc, num=num).capitalize()
    result = mat.get_percent_of_num(perc, num)

    return dict(
        question=question, answers=get_wrong_answers(result), difficult=difficult
    )


def get_perc_task_type_b(difficult: str = None) -> tuple:
    """
    Генерирует задачу на проценты.
    Найти число некое число, зная значение некоторого его процента.
    :param difficult: уровень сложности.
    :return: вопрос, кортеж с ответами, уровень сложности задачи.
    """
    template = get_random_template('B')

    # вычисления
    full_num = random.randrange(150, 1000, 10)
    perc = random.randrange(10, 90, 10)
    num = math.ceil(full_num*perc/100)

    # рендер вопроса
    question = template['question'].format(perc=perc, num=num).capitalize()
    result = mat.get_number_of_percent(perc, num)

    return dict(
        question=question, answers=get_wrong_answers(result), difficult=difficult
    )



def get_wrong_answers(answer: int = None) -> tuple:
    """
    Генерирует неправильные ответы в диапозоне +/- 50% от правильного ответа.
    :param answer: int правильный ответ
    :return: tuple правильный и список со всеми ответами
    """
    rang_v = math.ceil(answer/2)
    all_answers = [answer]
    for _ in range(3):
        all_answers.append(
            random.randint(answer-rang_v, answer+rang_v)
        )

    return answer, all_answers


def get_random_template(task_type=None, product=False):
    """Получает рандомный шаблон вопроса, или вопроса и товара"""
    templ = random.choice(TEMPLATES['PERCENT']['PERCENT_TASKS'][task_type])

    if product:
        staff = random.choice(TEMPLATES['PERCENT']['PERCENT_PRODUCT'])
        return templ, staff

    return templ


def test():
    print(get_perc_task_type_d())
