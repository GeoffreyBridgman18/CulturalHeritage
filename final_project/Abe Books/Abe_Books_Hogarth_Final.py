import requests
from bs4 import BeautifulSoup
import time
import csv

csv_file_path = "url_generator.csv"
output_csv = "abe_data.csv"

with open(output_csv, mode='w', newline='') as csv_file:
    # CSV writer
    csv_writer = csv.writer(csv_file)
    # Write header row
    csv_writer.writerow(["Title", "Author", "Price"])

    total_items = 0

    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        urls = [row[0] for row in reader]

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        all_links = soup.find_all("a", {"itemprop": "url"})

        for link in all_links:
            href = f"https://www.abebooks.com{link['href']}"
            item_page = requests.get(href)

            if item_page.status_code == 200:
                item_page_soup = BeautifulSoup(item_page.text, "html.parser")

                title_box = item_page_soup.find("h1", id="book-title")

                if title_box:
                    abe_title = title_box.find("span", class_="main-heading").text
                    print(abe_title)

                    price_box = item_page_soup.find("div", class_="basket-price")

                    if price_box:
                        abe_price = price_box.find("span", id="book-price").text
                        print(abe_price)

                        author_box = item_page_soup.find("h2", id="book-author")

                        if author_box:
                            abe_author = author_box.find("a").text
                            print(abe_author)

                            total_items += 1

                            csv_writer.writerow([abe_title, abe_author, abe_price])
            time.sleep(0.25)

    # Print the total number of items
    print(f"Total number of items: {total_items}")
