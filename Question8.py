import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"
headers = {"User-Agent": "Mozilla/5.0"}
# Identify url and use headers in order to make the request
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
# Make the request and parse the HTML

content = soup.find("div", id="mw-content-text")
# Create a variable for the main content area

headings = []
for h2 in content.find_all("h2"):
    text = h2.get_text(strip=True)
# for all h2 in the main content area store it in a variable called text

    text = text.replace("[edit]", "").strip()
# The Headers in the url have an [edit] beside them, so replace it with "" and remove the extra whitespace

    skip_terms = ["References", "External links", "See also", "Notes"]
    if any(term in text for term in skip_terms):
        continue
# For any unwanted text in the skip_terms variable do not append to headings

    headings.append(text)
# Append the text to headings

with open("headings.txt", "w",encoding="utf-8") as file:
    for heading in headings:
        file.write(heading + "\n")
# Create the file and write the headings each on a new line

print(f"Saved {len(headings)} headings to headings.txt")
# Print the total amount of headings saved and written to headings.txt




