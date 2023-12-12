import cloudscraper
from bs4 import BeautifulSoup
import csv
import time  # Import the time module for adding delays

csv_file = "checklist_hogarth_press.csv"
output_csv_file = "ebay_data_matches_control.csv"

scraper = cloudscraper.create_scraper()

# Open the output CSV file outside the loop
with open(output_csv_file, 'w', newline='', encoding='utf-8') as output_csv:
    fieldnames = ["Title", "Authors",  "Date", "Price"]
    writer = csv.writer(output_csv)
    writer.writerow(fieldnames)  # Write the header

    total_items = 0  # Initialize the total items counter

    for current_page in range(1, 21):  # Adjust the range as needed
        if current_page == 1:
            url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=the+hogarth+press&_sacat=0&_ipg=240"
        else:
            url = f"https://www.ebay.com/sch/i.html?_from=R40&_nkw=the+hogarth+press&_sacat=0&_ipg=240&_pgn={current_page}"

        page_to_scrape = scraper.get(url)
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")

        all_links = soup.find_all("a", class_="s-item__link")

        for link in all_links:
            href = link.get('href')
            print("got the links at least")

            volume_data = {"ebay_title": "N/A", "ebay_price": "N/A"}

            item_page = scraper.get(href)
            item_soup = BeautifulSoup(item_page.text, "html.parser")

            h1_element = item_soup.find("h1", class_="x-item-title__mainTitle")
            if h1_element:
                title_element = h1_element.find("span", class_="ux-textspans ux-textspans--BOLD")
                volume_data["ebay_title"] = title_element.text.strip()

            price_container = item_soup.find("div", class_="x-price-primary")
            if price_container:
                price_element = price_container.find("span", class_="ux-textspans")
                volume_data["ebay_price"] = price_element.text.strip()

            with open(csv_file, 'r', encoding='utf-8') as csv_file_read:
                csv_reader = csv.DictReader(csv_file_read)
                for row in csv_reader:
                    csv_title = row['Title'].strip()

                    if csv_title.lower() in volume_data["ebay_title"].lower():
                        print("Match found in CSV:")
                        print(f"Title: {row['Title']}")
                        print(f"Author: {row['Author']}")
                        print("\n")

                        writer.writerow([csv_title, row["Author"].strip(), row["Date"].strip(), volume_data["ebay_price"]])

                        total_items += 1  # Increment the total items counter

            # Add a delay to avoid being blocked
            time.sleep(0.25)

    print(f"Total number of items on all pages: {total_items}")