"""Task Three"""


import base64
import requests


def pictures(path, name):
    """Wel, I tried"""
    request = requests.post('https://postman-echo.com/post', files={'file': path})
    with open(name, 'w') as file:
        decoded = base64.b64decode(request.json()['files']['file'].split(',')[-1]).decode('utf-8')
        file.write(decoded)


pictures(r'Оптимизированное шокладное печенье.jpg', 'cookies.jpg')
