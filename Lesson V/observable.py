"""Task 3"""


class Observable:
    """Well, it's a class"""
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        public = [attr for attr in self.__dict__ if not attr.startswith("_")]
        result = ''
        for attr in public:
            result += attr + '=' + str(self.__dict__[attr]) + ', '
        return result[:-2]


class Child(Observable):
    """And another one"""
    pass


X = Child(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
print(X)
print(X.foo)
print(X._bazz)
