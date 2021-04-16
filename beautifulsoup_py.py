#!/bin/python3
from bs4 import BeautifulSoup

# Load html file.
filename='some.html'
with open(filename, 'r') as f:
    contents = f.read()
soup = BeautifulSoup(contents, 'lxml')  # 'html.parser'

# If you just want a string, with no fancy formatting, you can call str() on a BeautifulSoup object 
str(soup)

# Print pretty.
print(soup.prettify())

# Read table
data = []
table = soup.find('table', attrs={'class':'lineItemsTable'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values
print(data)

# Find parent.
from bs4 import BeautifulSoup
html = open("medium.html").read()
soup = BeautifulSoup(html)
tag = soup.find("div", text="inner")
print(tag.find_parent('div'))
#~ OUTPUT
#~ <div>middle
      #~ <div>inner</div>
#~ </div>
# ----------------------
from bs4 import BeautifulSoup
import re

html = '<body><div>changing text</div><div>fixed text</div><body>'
soup = BeautifulSoup(html)
x = soup.body.findAll(text=re.compile('fixed text'))[0].parent.previous_sibling
assert x.text == 'changing text'


# ----------------------------------
#!/bin/python3
from bs4 import BeautifulSoup

mytxt = """
<h1>Hello World</h1>
<p>This is a <a href="http://example.com">link</a></p>
<td>
    <p></p>
    <div>HIDDEN</div>
</td>
"""

soup = BeautifulSoup(mytxt, 'lxml')
print(soup.text)

# Remove all attributes, e.g. style, class, etc.
def removeAttributes(soup):
    for x in soup.find_all():
        x.attrs = None
        
    return soup