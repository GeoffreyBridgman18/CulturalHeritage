import requests
import json
import re
import csv

total_books = 0
max_results = 5000
good_books = []

csv_file = "checklist_hogarth_press.csv"
output_csv_file = "output_lenient_Google_title_matches_control.csv"
google_api_output_file = "Google_API.csv"  # New CSV file for Google API data
books_data = []

with open(output_csv_file, 'w', newline='', encoding='utf-8') as output_csv:
    fieldnames = ["Title", "Authors", "Publisher", "Date", "Match Found"]
    writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
    writer.writeheader()

    while total_books < max_results:
        api_key = "AIzaSyBfJx2J-4eByBcXg-kqaGRnsf6CAtJcieU"
        url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            "q": "inpublisher:\"hogarth press\"",
            "key": api_key,
            "maxResults": 40,
            "startIndex": total_books
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, params=params)
        data = response.json()

        items = data.get('items', [])

        if not items:
            break

        for book in items:
            google_volume_info = book.get('volumeInfo', {})
            google_title = google_volume_info.get('title', 'N/A')
            google_authors = google_volume_info.get('authors', ['N/A'])
            google_publisher = google_volume_info.get('publisher', 'N/A')
            google_date = google_volume_info.get('publishedDate', 'N/A')

            total_books += len(items)

            # Print Google API data
            print(f'Google Title: {google_title}\nAuthors: {google_authors}\nPublisher: {google_publisher}\nDate: {google_date}\n')

            # Write Google API data to the new CSV file
            with open(google_api_output_file, 'a', newline='', encoding='utf-8') as google_api_csv:
                google_api_writer = csv.writer(google_api_csv)
                google_api_writer.writerow(["Title", "Author", "Publisher", "Date"])
                google_api_writer.writerow([google_title, ', '.join(google_authors), google_publisher, google_date])

            # Assuming your CSV file has a 'Title' column, adjust as needed
            with open('checklist_hogarth_press.csv', 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    csv_title = row['Title'].strip()
                    csv_publisher = "Hogarth Press"
                    csv_author = row["Author"].strip()
                    csv_date = row["Date"].strip()

                    # Check if the CSV title is part of the Google title
                    if csv_title.lower() in google_title.lower():
                        print("Match found in CSV:")
                        print(f"Title: {row['Title']}")
                        print(f"Author: {row['Author']}")
                        print(f"Publisher: {row['Publisher']}")
                        print(f"Date: {row['Date']}\n")

                        # Write the match to the output CSV file
                        writer.writerow({
                            "Title": csv_title,
                            "Authors": csv_author,
                            "Publisher": csv_publisher,
                            "Date": csv_date,
                            "Match Found": "Yes",
                        })

                        # Break the loop to move to the next Google book
                        break

            print("\n")

# Print the total book count after the loop
print(f'Total Books Processed: {total_books}')

