import csv

title_count = {}
title_prices = {}

with open('ebay_data_matches_control.csv') as file:
    processed_csv = csv.DictReader(file)
    for row in processed_csv:
        title = row['Title']

        # Count occurrences of each title
        title_count[title] = title_count.setdefault(title, 0) + 1

        # Extract and sum total price values per title
        price_str = row['Price']
        price = float(''.join(c for c in price_str if c.isdigit() or c == '.'))
        title_prices[title] = title_prices.setdefault(title, 0) + price

print("Title Details:")
for title, count in title_count.items():
    total_price = title_prices[title]
    average_cost = total_price / count

    print(f"{title}:")
    print(f"  Count: {count}")
    print(f"  Sum Total of Prices: ${total_price:.2f}")
    print(f"  Average Cost: ${average_cost:.2f}")
    print("\n")


    



   
