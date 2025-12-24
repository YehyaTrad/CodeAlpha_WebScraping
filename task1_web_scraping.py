print("RUNNING FILE:", __file__)

import requests

url = "http://books.toscrape.com/"
response = requests.get(url)

print(response.status_code)

# -------------------
# SCRAPING CODE
# -------------------
import requests
from bs4 import BeautifulSoup
import pandas as pd



book_list = []

for page in range(1, 51):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)

    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        stock = book.find("p", class_="instock availability").text.strip()

        book_list.append({
            "Title": title,
            "Price": price,
            "Stock": stock
        })

df = pd.DataFrame(book_list)
df.to_csv("books_raw_data.csv", index=False)

print("Raw dataset saved!")


# -------------------
# CLEANING CODE
# -------------------
import re

df = pd.read_csv("books_raw_data.csv")

df["Price"] = df["Price"].astype(str).apply(
    lambda x: re.sub(r"[^0-9.]", "", x)
)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

df["Stock"] = df["Stock"].apply(
    lambda x: 1 if "In stock" in x else 0
)

df.dropna(subset=["Price"], inplace=True)
df.drop_duplicates(inplace=True)

df.to_csv("books_cleaned_data.csv", index=False)

print("✅ Cleaned dataset saved successfully!")
