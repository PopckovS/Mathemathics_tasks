import random
from utils.util import get_operation_division

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
    operations = get_random_operations(min_op=3, max_op=7, use_one=(':',), not_use=())
    expressions = str()
    division = []
    num_list = []

    # create number for expression
    for iter in range(len(operations)):
        current = operations[iter]
        num = random.randint(1, 10)

        if current == '+' or current == '-':
            num_list.append(num)
        elif current == ':':
            num_list += [*get_operation_division()]
            division += [*get_operation_division()]  #  FIXME
        elif current == '*':
            num_list.append(num)

        if len(operations) == iter+1:
            if ':' in operations:
                continue
            random.randint(1, 10)

    # create expression
    for num in num_list:
        expressions = [''.join(str(x)) for x in zip(num_list, operations)]

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
    count = random.randint(min_op, max_op)
    operations = list()

    # generating mathematical operations
    while len(operations) < count:
        op = random.choice(OPERATORS)
        if (op in use_one and op in operations) or (op in not_use):
            continue
        operations.append(op)
    return tuple(operations)


def test():
    print(get_expressions())
    # print(get_random_operations(max_op=5, use_one=[':']))
