import math

"""
Функции для математической обработки.
"""


def get_percent_of_num(perc, num):
    """Возвращает искомый процент от числа"""
    return math.ceil((num / 100) * perc)


def get_number_of_percent(perc, perc_v):
    """Возвращает число, зная процент и значение этого процента от целого числа"""
    return math.ceil((perc_v*100)/perc)


def get_percent(num, denominator):
    """Возвращает процент который одно число составляет от другого"""
    return math.ceil((num/denominator)*100)




