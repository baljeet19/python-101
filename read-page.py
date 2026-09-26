# This script reads a table from a Google Docs document and outputs the data in JSON format.
# Read plain text or HTML from a Google Docs document and parse it to extract table data.
# py -m pip install requests
# 
# py -m pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
import json

url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
table_class = "c7"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=20)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

table = soup.select_one(f"table")#.{table_class}

if table is None:
    raise ValueError(f'Table class "{table_class}" was not found.')

header_cells = table.select("thead th")

if not header_cells:
    first_row = table.find("tr")

    if first_row is None:
        raise ValueError("The table has no rows.")

    header_cells = first_row.find_all(["th", "td"])

column_names = [
    cell.get_text(" ", strip=True)
    for cell in header_cells
]

data_rows = table.select("tbody tr")

if not data_rows:
    data_rows = table.find_all("tr")[1:]

data = []

for row in data_rows:
    cell_values = [
        cell.get_text(" ", strip=True)
        for cell in row.find_all("td")
    ]

    if cell_values:
        data.append(dict(zip(column_names, cell_values)))

print(json.dumps(data, ensure_ascii=False, indent=2))