"""Task One"""


import requests


def html_size(link):
    """Return the size of an HTML document"""
    response = requests.get(link)
    return len(response.text)
    
    
print(html_size('https://google.com'))
