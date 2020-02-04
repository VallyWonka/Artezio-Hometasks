"""
Lesson III, Task 1
"""


TEST_TUPLE = (2, 6, 9, 34)
TEST_LIST = [56, 8, 4, 7]


def squares(array):
    """
    Returns a list of squares of all the elements in a given array
    """
    return [arg ** 2 for arg in array]


# print(squares(TEST_TUPLE))
# print(squares(TEST_LIST))


def even_positions(array):
    """
    Returns elements in even positions in a given array
    """
    return list(filter(lambda elem: (array.index(elem) + 1) % 2 == 0, array))


# print(even_positions(TEST_LIST))
# print(even_positions(TEST_TUPLE))


def cubes_odd_positions(array):
    """
    Returns cubes of numbers in odd positions in a given array
    """
    return [elem ** 3 for elem in array if (array.index(elem) + 1) % 2 != 0]


# print(cubes_odd_positions(TEST_TUPLE))
# print(cubes_odd_positions(TEST_LIST))
