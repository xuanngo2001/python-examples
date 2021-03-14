#!/bin/python3

# Load html file.
with open(filename, 'r') as f:
    contents = f.read()
soup = BeautifulSoup(contents, 'lxml')  # 'html.parser'

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