#!/bin/python3

from urllib.parse import urlparse

url = "http://spacbus-test/spac-price-json"
u = urlparse(url)
print(u.scheme)
print(u.netloc)
print(u.path)
print(u) # ParseResult(scheme='http', netloc='spacbus-test', path='/spac-price-json', params='', query='', fragment='')
