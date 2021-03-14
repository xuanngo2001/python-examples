#!/bin/python3

import urllib.request

# Download url.
url="https://google.com"
with urllib.request.urlopen(url) as url:
    data = url.read()
    
# Save to file.
with open('google.html', 'wb') as f:
    f.write(data)
    
# Simulate a browser.
req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
with urllib.request.urlopen(req) as url:
    data = url.read()
