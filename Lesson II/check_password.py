"""
Task 5 from Lesson Two
"""


USER_PASSWORD = {'Tatarstan116': 'qwerty0987', 'Python3_7': 'hello_World'}

USERNAME = input('Please enter your username: ')
while USERNAME not in USER_PASSWORD:
    USERNAME = input('No such user.\nPlease try again: ')
print('Your username is correct.')

PASSWORD = input('Please enter your password: ')
while USER_PASSWORD[USERNAME] != PASSWORD:
    PASSWORD = input('Password for user: {} is incorrect.\nPlease try again: '.format(USERNAME))
print('Password for user: {} is correct.'.format(USERNAME))
