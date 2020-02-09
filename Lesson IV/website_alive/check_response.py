"""Module Two"""


from website_alive.make_request import make_request as mr


def check_response(url):
    """Checks response"""
    if mr(url).status_code == 200:
        return True
    return False


# print(check_response('https://vk.com/vladimirputin_rf'))
# print(check_response('https://vk.com/lol'))
