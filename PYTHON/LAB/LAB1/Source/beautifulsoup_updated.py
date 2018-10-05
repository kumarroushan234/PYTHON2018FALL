import requests
from bs4 import BeautifulSoup
import os
import csv
url  = 'https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2015'
page = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.title.text)
table = soup.find('table')

# get the table header
columns = table.find_all('th')

# Get the table rows
rows = table.find_all('tr')

no_of_rows = len(rows)

# Write the table data into a csv file
with open('output1.csv', 'w') as f:
    column_names = [col.text for col in columns]
    column_names = str(column_names)
    column_names = column_names.replace('[','').replace(']','')
    f.write(column_names)
    for row in rows[1:no_of_rows]:
        table_row = row.find_all('td')
        row_values = [r.text for r in table_row]
        row_values = str(row_values)
        row_values = row_values.replace('[','').replace(']','')
        f.write('\n')
        f.write(row_values)
