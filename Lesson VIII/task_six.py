"""Task Six"""


import re


STRING = 'Buffalo buffalo buffalo buffalo buffalo?'


if re.fullmatch(r'^((?=.*[a-zA-Z]).{2,}){4,}.\?$', STRING):
    print('YES')
else:
    print('NO')
