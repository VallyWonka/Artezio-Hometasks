"""Task One"""


from time import sleep


def average_time(num=2):
    """Decorator"""
    def inner(function):
        last_calls = []

        def wrapper(arg):
            result = function(arg)
            last_calls.append(result)
            if len(last_calls) < num:
                print(f'Среднее время работы функции: {result * 1000} мс.')
            else:
                print(f'Среднее время работы функции: {int(sum(last_calls[-num:]) / num * 1000)} мс.')
                del last_calls[0]
            return result
        return wrapper
    return inner
                

@average_time(num=3)
def func(sec):
    """Random Function"""
    sleep(sec)
    return sec


func(3)
func(7)
func(1)
func(8)
