"""Task 1"""


from math import sqrt


class Complex:
    """Complex numbers"""
    def __init__(self, string):
        parts = string.split()
        self.real = float(parts[0])
        self.imaginary = float(parts[1])

    def __add__(self, other):
        res_re = self.real + other.real
        res_im = self.imaginary + other.imaginary
        return Complex('{} {}'.format(res_re, res_im))

    def __sub__(self, other):
        res_re = self.real - other.real
        res_im = self.imaginary - other.imaginary
        return Complex('{} {}'.format(res_re, res_im))

    def __mul__(self, other):
        res_re = self.real * other.real - self.imaginary * other.imaginary
        res_im = self.real * other.imaginary + self.imaginary * other.real
        return Complex('{} {}'.format(res_re, res_im))

    def __div__(self, other):
        res_nom = self.__mul__(Complex('{} {}'.format(other.real, other.imaginary * -1)))
        res_denom = other.real ** 2 - other.imaginary ** 2
        return '{} / {}'.format(res_nom, res_denom)

    def __abs__(self):
        result = sqrt(self.real ** 2 + self.imaginary ** 2)
        return result

    def __str__(self):
        operator = '+' if self.imaginary >= 0 else ''
        return '{:.2f}{}{:.2f}i'.format(self.real, operator, self.imaginary)


C = Complex('3 4')
D = Complex('-0.25 -4')

print(C)
print(D)
print(C + D)
print(C - D)
print(C * D)
print(C.__div__(D))
print(abs(C))
print(abs(D))
