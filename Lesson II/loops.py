"""
Hometasks 1-4 from Lesson Two
"""


def square_odd_numbers(stop):
    """
    Counts the squares of all the odd numbers in the segment [0, x]
    """
    counter = 0
    for i in range(stop + 1):
        if i % 2 != 0:
            print(i**2)
            counter += 1
    print('There are {} odd numbers within the segment'.format(counter))


# square_odd_numbers(9)
# square_odd_numbers(18)


def multiples(start, stop, denom):
    """
    Counts multiples for c within (a, b) interval
    """
    counter = 0
    for i in range(start + 1, stop):
        if i % denom == 0:
            counter += 1
    print('There are {} multiples within the interval'.format(counter))


# multiples(100, 467, 44)
# multiples(0, 10, 2)


def factorial(number):
    """
    Counts the factorial of the given number
    """
    counter = 1
    for i in range(1, number + 1):
        counter *= i
    print('{}! = {}'.format(number, counter))


# factorial(5)
# factorial(10)


def old_range(stop, start=0, step=1):
    """
    Python 2.x's range
    """
    stop = stop - 1 if stop > 0 else stop + 1
    range_list = [start]
    while abs(stop - start) >= abs(step):
        start += step
        range_list.append(start)
    return range_list


# print(old_range(5))
# print(old_range(17, 5))
# print(old_range(-17, 5, -3))
