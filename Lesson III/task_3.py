"""
Lesson III, Task 3
"""


MAX = 0


def numbers(num_1, num_2, num_3, num_4):
    """
    Does things
    """
    numbers = [num_1, num_2, num_3, num_4]
    global MAX
    if max(numbers) > MAX:
        MAX = max(numbers)
    mean = sum(numbers) / 4
    return mean, MAX


# print(numbers(1, 2, 3, 4))
# print(numbers(-3, -2, 10, 1))
# print(numbers(7, 8, 8, 1))
