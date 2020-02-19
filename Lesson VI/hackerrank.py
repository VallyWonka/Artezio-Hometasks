"""I wasn't sure whether you would find the task on hackerrank, so"""


constraints = int(input())

for i in range(constraints):
    try:
        a, b = map(int, input().split())
        result = a // b
    except ZeroDivisionError as ZDE:
        print('Error Code:', ZDE)
    except ValueError as VE:
        print('Error Code:', VE)
    else:
        print(result)
