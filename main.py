"""Main File"""


import website_alive.check_response as cr


USER_URL = input('Paste a url address: ')


print(cr.check_response(USER_URL))
