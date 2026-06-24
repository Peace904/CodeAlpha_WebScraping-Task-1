import requests
from bs4 import BeautifulSoup
import pandas as pd

book_data = []

# Scrape the first 5 pages
for page in range(1, 6):

    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find("p", class_="instock availability").text.strip()

        book_data.append({
            "Title": title,
            "Price": price,
            "Availability": availability
        })

df = pd.DataFrame(book_data)

df.to_csv("scraped_data.csv", index=False)

print(f"Successfully scraped {len(book_data)} books!")
print(df.head())