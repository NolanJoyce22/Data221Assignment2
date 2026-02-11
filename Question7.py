import requests
from bs4 import BeautifulSoup

data_science_url = "https://en.wikipedia.org/wiki/Data_science"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(data_science_url, headers=headers)
# Identify the url and make the request using headers

soup = BeautifulSoup(response.text, "html.parser")
# Parse the HTML using BeautifulSoup

title = soup.find("title").get_text()
print("Page title:")
print(title)
# Pull the title from the page and print it

content_div = soup.find("div", id = "mw-content-text")
parser_output = content_div.find("div", class_="mw-parser-output")
paragraphs = content_div.find_all("p")
# Find all paragraphs from the page

first_paragraph = None

for p in paragraphs:
    text = p.get_text(strip=True)
    if len(text) >= 50:
        first_paragraph = text
        break

# loop through all the paragraphs removing the whitespace using strip=True
# If the paragraph has 50 or more characters the condition is met and the loop is broken

print("First paragraph (50+ characters):")
print(first_paragraph)

