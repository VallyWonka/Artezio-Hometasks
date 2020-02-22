"""Task Four"""


import inspect


def checker(function):
    """Decorator"""
    def wrapper(*args):
        inspection = inspect.getfullargspec(function)
        if not inspection.annotations or len(inspection.args) > len(inspection.annotations):
            raise LookupError('Annotation is not complete or does not exist.')
        for name, _type in inspection.annotations.items():
            argument = args[inspection.args.index(name)]
            if not isinstance(argument, _type):
                print(f'{argument} is not of the type {_type}')
        return function
    return wrapper


@checker
def func(arg_a: int, arg_b: str, arg_c: list):
    """Random function"""
    print(arg_a, arg_b, arg_c)


func(5, 'PizzA', [1, 3, 6])
