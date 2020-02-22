"""Task Three"""


def carry(function):
    """Carrying"""
    def wrapper_1(arg_1):
        def wrapper_2(arg_2):
            return function(arg_1, arg_2)
        return wrapper_2
    return wrapper_1


@carry
def func(abc, deb):
    """Random function"""
    return abc + deb


RES = func(2)(5)
print(RES)
