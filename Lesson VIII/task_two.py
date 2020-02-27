"""Task Two"""


import requests


def currency_converter(num, curr_1, curr_2):
    """It's a currency converter"""
    response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{curr_1}')
    result = num * response.json()['rates'][curr_2]
    return result


print(currency_converter(10.0, 'RUB', 'EUR'))
