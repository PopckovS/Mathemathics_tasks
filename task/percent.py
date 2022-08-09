import math
import random

from utils import util
from .templates import TEMPLATES

"""
The generator of tasks for percentages.

Percentage tasks are divided into categories:
A - Find percentages of the number.
B - Find a number by knowing the value of some percentage of it.
C - Find how much a number is a percentage of another number.
D - Find the difference in % between 2 numbers.

Генерация математических задачек на проценты.

Задачи на проценты разделены по категориям:
A - Найти процента от числа.
B - Найти число, зная значение некоторого его процента.
C - Найти сколько число составляет процентов от другого числа.
D - Найти разницу в % между 2 числами.
"""


def get_perc_task_type_a(difficult: str = None) -> tuple:
    """
    Find the percentage of the number.
    :param difficult: str - the difficulty level of the question.
    :return: dict - a question, a tuple with answers, the difficulty level of the task.
    """
    template = get_random_percent_template('A')

    # calculations
    num = random.randrange(150, 1000, 10)
    perc = random.randrange(10, 90, 10)

    # question rendering
    question = template['question'].format(perc=perc, num=num).capitalize()
    result = util.get_percent_of_num(perc, num)

    return dict(
        answer=result,
        question=question,
        difficult=difficult,
        answers=util.get_wrong_answers(result)
    )


def get_perc_task_type_b(difficult: str = None) -> tuple:
    """
    Find a number a certain number, knowing the value of a certain percentage of it.
    :param difficult: str - the difficulty level of the question.
    :return: dict - a question, a tuple with answers, the difficulty level of the task.
    """
    template = get_random_percent_template('B')

    # calculations
    full_num = random.randrange(150, 1000, 10)
    perc = random.randrange(10, 90, 10)
    num = math.ceil(full_num*perc/100)

    # question rendering
    question = template['question'].format(perc=perc, num=num).capitalize()
    result = util.get_number_of_percent(perc, num)

    return dict(
        answer=result,
        question=question,
        difficult=difficult,
        answers=util.get_wrong_answers(result)
    )


def get_perc_task_type_c(difficult: str = None) -> tuple:
    """
    Find how much one number is a percentage of another number.
    :param difficult: str - the difficulty level of the question.
    :return: dict - a question, a tuple with answers, the difficulty level of the task.
    """
    template = get_random_percent_template('C')

    # calculations
    num_1 = random.randrange(150, 1000, 10)
    perc = random.randrange(10, 90, 10)/100
    num_2 = math.ceil(num_1*perc)

    # question rendering
    question = template['question'].format(num_1=num_2, num_2=num_1).capitalize()
    result = util.get_percent(num=num_2, denominator=num_1)

    return dict(
        answer=result,
        question=question,
        difficult=difficult,
        answers=util.get_wrong_answers(result)
    )


def get_perc_task_type_d(difficult: str = None) -> dict:
    """
    Knowing 2 numbers, find the difference between them as a percentage.
    :param difficult: str - the difficulty level of the question.
    :return: dict - a question, a tuple with answers, the difficulty level of the task.
    """
    template, staff = get_random_percent_template('D', product=True)

    # calculations
    result = random.randrange(10, 90, 10)

    if template['meta'] == "price up":
        cost_old = random.randrange(150, 500, 10)
        perc = (result/100)+1
        cost_new = math.ceil(cost_old*perc)
    elif template['meta'] == "price down":
        cost_old = random.randrange(150, 1000, 10)
        perc = result/100
        cost_new = math.ceil(cost_old-(cost_old*perc))

    # question rendering
    question = template['question'].format(
        name=staff, cost_old=cost_old, cost_new=cost_new).capitalize()

    return dict(
        answer=result,
        question=question,
        difficult=difficult,
        answers=util.get_wrong_answers(result)
    )


def get_random_percent_template(task_type=None, product=False):
    """
    Gets a random question template, or a question and a product
    :param task_type: str - get a specific type of task.
    :param product: str - get random product or not.
    :return: dict; [dict, str] task and product.
    """
    templ = random.choice(TEMPLATES['PERCENT']['PERCENT_TASKS'][task_type])

    # get product
    if product:
        staff = random.choice(TEMPLATES['PERCENT']['PERCENT_PRODUCT'])
        return templ, staff
    return templ


def test():
    print(get_perc_task_type_d())

