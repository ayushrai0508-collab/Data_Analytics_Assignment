DATA ANALYTICS ASSIGNMENT

Name: Ayush Rai
Course: B.tech(CSE)
________________________________________
TASK 1: WEB SCRAPING USING PYTHON
Objective
The objective of this task is to extract data from a website using Python libraries such as Requests and BeautifulSoup and store the extracted information in a CSV file.
Tools Used
• Python
• Requests
• BeautifulSoup
• Pandas
• Visual Studio Code
Code:
Code Screenshot:-
 <img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/dc5a6e79-5cb5-4140-a74d-f470de290219" />

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

Output
 <img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/8061ccac-3067-40bf-ba4f-ef93cd8d8431" />


Result
The program successfully scraped quote and author information from the website and stored the extracted data in a CSV file named quotes_dataset.csv.
Conclusion
Web scraping was successfully performed using BeautifulSoup. The extracted information was organized into a structured dataset and exported for further analysis.
