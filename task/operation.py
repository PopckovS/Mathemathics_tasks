import random
from utils.util import get_operation_division
from .context_exception import ArgumentException

"""
Tasks for mathematical operations.
"""

# all possible operations
OPERATORS = ["+", "-", "*", ":"]


def get_expressions():
    """
    Generate an expression
    :return:
    """
    operations = get_random_operations(
        min_op=5, max_op=7, use_one=(), not_use=())
    expressions = str()
    division = []
    num_list = []

    # create number for expression
    for iter in range(len(operations)):
        current = operations[iter]
        num = random.randint(1, 10)

        if current in ('+', '-', '*'):
            num_list.append(num)
        elif current == ':':
            num_list += [*get_operation_division()]

        if len(operations) == iter+1:
            if ':' in operations:
                continue
            num_list.append(random.randint(1, 10))
    # # create number for expression
    # for iter in range(len(operations)):
    #     current = operations[iter]
    #     num = random.randint(1, 10)
    #
    #     if current in ('+', '-', '*'):
    #         num_list.append(num)
    #     elif current == ':':
    #         num_list += [*get_operation_division()]
    #
    #     if len(operations) == iter+1:
    #         if ':' in operations:
    #             continue
    #         random.randint(1, 10)

    # create expression

    # for op in operations:
    #     expressions += f'num_list.pop(0)}] {op}'

    # TODO get answer

    return dict(
        expressions=expressions,
        operations=operations,
        division=division,
        num_list=num_list,
        # all_answers=util.get_wrong_answers(answer)
    )


def get_random_operations(min_op: int = 1,
                          max_op: int = 1,
                          use_one: tuple = (),
                          not_use: tuple = ()
                          ) -> tuple:
    """
    Returns a random number of random arithmetic operations.
    :param min_op: int - min count of operations.
    :param max_op: int - max count of operations.
    :param use_one: tuple operations that occur once.
    :param not_use: tuple operations that are forbidden to use.
    :return: tuple random generation operations.
    """

    # check gotten arguments
    if (min_op > max_op) or not isinstance(min_op, int) or not isinstance(min_op, int):
        raise ArgumentException((min_op, max_op))
    elif not isinstance(use_one, tuple) or not isinstance(not_use, tuple):
        raise ArgumentException((use_one, not_use))

    count = random.randint(min_op, max_op)
    operations = list()

    # generating mathematical operations
    while len(operations) < count:
        op = random.choice(OPERATORS)
        # check operations
        if (op in use_one and op in operations) or (op in not_use):
            continue
        operations.append(op)

    return tuple(operations)


def test():
    print(get_expressions())
    # print(get_random_operations(max_op=5, use_one=[':']))
