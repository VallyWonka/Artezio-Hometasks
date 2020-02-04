"""
Lesson III, Task 5
"""


def a():
    s = input().split()
    s.sort(key=lambda x: abs(float(x)))
    return s[0]


print(a())
