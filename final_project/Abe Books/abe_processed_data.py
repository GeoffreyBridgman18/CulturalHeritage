import csv

title_count = {}
title_prices = {}

with open('cleaned_up_abe_data.csv') as file:
    processed_csv = csv.DictReader(file)
    for row in processed_csv:
        title = row['Title_hogarth_press']
        author = row['Author_hogarth_press']

        # Count occurrences of each title and author
        title_count[title] = title_count.setdefault(title, 0) + 1

        # Extract and sum total price values per title
        price_str = row['Price']
        price = float(''.join(c for c in price_str if c.isdigit() or c == '.'))
        title_prices[title] = title_prices.setdefault(title, 0) + price

# Create and write to the new CSV file
output_file_path = 'abe_processed_data.csv'

with open(output_file_path, 'w', newline='') as output_file:
    fieldnames = ['Title', 'Author', 'Count', 'Total_Price', 'Average_Cost']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)

    writer.writeheader()

    for title, count in title_count.items():
        total_price = title_prices[title]
        average_cost = total_price / count

        writer.writerow({
            'Title': title,
            'Author': author,  # Added 'Author' column
            'Count': count,
            'Total_Price': total_price,
            'Average_Cost': average_cost
        })

print(f"Processed data has been written to {output_file_path}.")
