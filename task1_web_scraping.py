import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://quotes.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []
authors = []

for quote in soup.find_all("span", class_="text"):
    quotes.append(quote.text)

for author in soup.find_all("small", class_="author"):
    authors.append(author.text)

df = pd.DataFrame({
    "Quote": quotes,
    "Author": authors
})

print(df.head())

df.to_csv("quotes_dataset.csv", index=False)

print("CSV file created successfully")