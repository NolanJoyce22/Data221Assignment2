import requests
from bs4 import BeautifulSoup
import csv

machine_learning_url = "https://en.wikipedia.org/wiki/Machine_learning"
headers = {"User-Agent": "Mozilla/5.0"}
# Identify the url and use headers in order for the request to be trusted
response = requests.get(machine_learning_url, headers=headers)
# Retrieve the HTML of the page
soup = BeautifulSoup(response.text, "html.parser")
# parse the HTML

content_div = soup.find("div", id = "mw-content-text")
parser_output = content_div.find("div", class_="mw-parser-output")
# Narrow table search to the main content area
data_tables = parser_output.find_all("table")
# Search for all data tables in main content area
target_table = None
# Define table variable

for table in data_tables:
    rows = table.find_all("tr")
    if len(rows) >= 4:
        target_table = table
        break

# Loop through the tables until one is found containing more the 3 rows
# Condition is set to 4 as each of the tables will contain a header


headers_row = target_table.find("tr")
th_tags = headers_row.find_all("th")
# Create table rows with corresponding column headers
headers = [th.get_text(strip=True) for th in headers_row.find_all('th')]



if th_tags:
    column_headers = [th.get_text(strip=True) for th in th_tags]
else:
    td_count = len(headers_row.find_all("td"))
    column_headers = [f"col{i+1}" for i in range(td_count)]
# If headers exist use the header as the column header. Else create a column header
# with the name col{i+1}


table_data = []

for row in target_table.find_all("tr")[1:]:
    cells = row.find_all(["td", "th"])
    row_data = [cell.get_text(strip=True) for cell in cells]
# Within target_table find all the cells and store them in row_data

    while len(row_data) < len(headers):
        row_data.append("")

    table_data.append(row_data)
# Create the table and store in table_data

with open("Wiki_table.csv", "w", newline = "", encoding = "utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(table_data)
# Create a csv file and write the table to the file

