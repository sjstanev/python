from functools import reduce


def sum_args(*args):
    """
    *args - If you do not know how many arguments that will be passed into your function,
    add a * before the parameter name in the function definition.

    **kwargs - If you do not know how many keyword arguments that will be passed into your function, add two asterisk:
    ** before the parameter name in the function definition.

    A lambda function is a small anonymous function. Can take any number of arguments, but can only have one expression.
    lambda arguments : expression
        x = lambda a, b : a * b
        print(x(5, 6))

    reduce() - Python’s reduce() implements a mathematical technique commonly known as `folding` or `reduction`.
    You’re doing a fold or reduction when you reduce a list of items to a single cumulative value.
    Python’s reduce() operates on any iterable—not just lists—and performs the following steps:
        1. Apply a function (or callable) to the first two items in an iterable and generate a partial result.
        2. Use that partial result, together with the third item in the iterable, to generate another partial result.
        3. Repeat the process until the iterable is exhausted and then return a single cumulative value.
    functools.reduce(function, iterable[, initializer])

    from functools import reduce

     def my_add(a, b):
        result = a + b
        print(f"{a} + {b} = {result}")
        return result

    numbers = [0, 1, 2, 3, 4]

    reduce(my_add, numbers)
    0 + 1 = 1
    1 + 2 = 3
    3 + 3 = 6
    6 + 4 = 10
    10

    :param args:
    :return sum of arguments:
    """
    print(args)
    print(type(args))
    initializer = 0
    result = reduce(lambda a, b: a + b, args, initializer)
    return result



print(sum_args(5,4,3,7))
