import math
import random

"""
Functions for mathematical processing.
"""


def get_percent_of_num(perc, num):
    """Returns the desired percentage of the number"""
    return math.ceil((num / 100) * perc)


def get_number_of_percent(perc, perc_v):
    """
    Returns a number, knowing the percentage and the value of this percentage of an integer
    """
    return math.ceil((perc_v*100)/perc)


def get_percent(num, denominator):
    """Returns the percentage that one number is from another"""
    return math.ceil((num/denominator)*100)


def get_wrong_answers(answer: int = None) -> tuple:
    """
    Generates incorrect answers in the range of +/- 50% of the correct answer.
    :param answer: int - right answer.
    :return: tuple - correct answer and false answers.
    """
    # response generation range
    rang_v = math.ceil(answer/2)
    all_answers = [answer]

    # generating 3 unique incorrect answers
    while len(all_answers) < 4:
        res = random.randint(answer - rang_v, answer + rang_v)
        if res == answer or res in all_answers:
            continue
        all_answers.append(res)

    return all_answers
