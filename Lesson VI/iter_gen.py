"""Lesson VI"""


# task 1
EXAMPLE = [3, 'h', 436, 'fhgfgh', 4466, 'ggg', 346700]
EVEN_IT = iter(EXAMPLE)
while True:
    try:
        OBJ = next(EVEN_IT)
        if EXAMPLE.index(OBJ) % 2 == 0:
            print(OBJ)
    except StopIteration:
        break


# task 2
OBJ = 'hey hello'
PUBLIC_ATTR = [attr for attr in dir(OBJ) if not attr.startswith('_')]
print(PUBLIC_ATTR)


# task 3
KEYS_1 = ['one', ('two', 'three'), 4]
VALUES_1 = [5, 6]
KEYS_2 = ['a', 'the', 'as']
VALUES_2 = ['to', 'for', 'of', 'at']

def dictionary(keys, values):
    keys.extend([None for _ in range(len(values) - len(keys))])
    values = values[:len(keys) + 1]
    return {key: value for key, value in zip(keys, values)}


print(dictionary(KEYS_1, VALUES_1))
print(dictionary(KEYS_2, VALUES_2))


# task 4
def cycle(item):
    while True:
        for i in iter(item):
            yield i


# for i in cycle('DOG'):
#     print(i)


# task 5
def chain(*args):
    for elem in args:
        try:
            iter(elem)
        except TypeError:
            yield elem
        else:
            for item in elem:
                yield item


for item in chain(10, 'rrr', 'hey', 'hello', ('sociolinguistics', 'theory of language'), ['i', 'love', 'cats']):
    print(item, end=', ')
