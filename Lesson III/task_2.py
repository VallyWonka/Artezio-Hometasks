"""
Lesson III, Task 2
"""


def mul_sum(*args, **kwargs):
    """
    Does things
    """
    list_args = list(args)
    list_args.extend(dict(kwargs).values())
    all_args = []

    def flatten(array):
        for item in array:
            if isinstance(item, (list, tuple)):
                try:
                    flatten(item)
                except RecursionError:
                    print('Circular linked item found')
                    all_args.clear()
                    break
            else:
                all_args.append(item)
        return all_args if all_args else None
    if flatten(list_args):
        if 0 in all_args:
            all_args.remove(0)
        sum_ = sum(all_args)
        mul = 1
        for elem in all_args:
            mul *= elem
        return sum_, mul
    return None


# B = (3, 4, [5, 6, [7, 8], []])
# B[2][3].append(B)
# print(mul_sum(1, 2, [3, 4, (5, 6)], a=(10, 11), b=B))
