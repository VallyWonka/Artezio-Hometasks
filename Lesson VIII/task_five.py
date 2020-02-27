"""Task Five"""


import re


if re.fullmatch('(?=.+[a-z])(?=.+[A-Z])(?=.+[0-9])(?=.[_*%&]*).{8,12}', 'aaZZ0199&666'):
    print('YES')
else:
    print('NO')
