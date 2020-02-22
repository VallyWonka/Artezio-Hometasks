"""Task Two"""


from time import sleep, time


def time_methods(*args):
    """Decorator"""
    def inner(obj):
        def wrapper(arg):
            sample = obj(arg)
            for item in args:
                if item in dir(obj):
                    time_1 = time()
                    sample.__getattribute__(item)
                    print((time() - time_1) * 1000)
            return sample
        return wrapper
    return inner


@time_methods('inspect', 'foo')
class Spam:
    """Random Class"""
    def __init__(self, arg):
        self.arg = arg

    def inspect(self):
        """Sleepy"""
        sleep(self.arg)
        return "Hi!"

    def barr(self):
        """Drunk"""
        return self.arg


A = Spam(20)
