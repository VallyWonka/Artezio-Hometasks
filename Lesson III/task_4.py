"""
Lesson III, Task 4
"""


import re


def depth(string):
    """
    Sorry, didn't finish it. Don't even know whether I was thinking in the right direction
    """
    tags = string.split('><')[1:-1]
    well_idk = {'name': 'root', 'children': []}
    for ind, tag in enumerate(tags):
        tag = re.sub(r'\W', '', tag)
        tags[ind] = tag

    def interpretation(tags_array):
        for tag in tags_array:
            if tags.count(tag) == 1:
                nonlocal _depth
                _depth += 1
                tags.remove(tag)
                return {'name': tag, 'children': []}
            back_ind = -tags_array.index(tag)
            for _ in range(2):
                tags.remove(tag)
            return {'name': tag, 'children': [interpretation(tags_array[1:back_ind])]}

    _depth = 0
    for tag in tags:
        well_idk['children'].append(interpretation(tags))
    print(well_idk, _depth)


A = '<root><element1 /><element2 /><element3><element4><element5 /></element4></element3></root>'
depth(A)
