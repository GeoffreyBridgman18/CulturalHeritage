import csv

abe_titles = {}

# Process abe_data.csv to create a dictionary of titles and corresponding author and price
with open('abe_data.csv') as abe_file:
    abe_csv = csv.DictReader(abe_file)
    for row in abe_csv:
        title = row['Title'].lower()  # Convert to lowercase for case-insensitive comparison
        abe_titles[title] = {'Author': row['Author'], 'Price': row['Price']}

# Create and write to the new CSV file
output_file_path = 'abe_clean_data.csv'

with open(output_file_path, 'w', newline='') as output_file:
    fieldnames = ['Title', 'Author', 'Price']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)

    writer.writeheader()

    # Process checklist_hogarth_press.csv and check for matches
    with open('checklist_hogarth_press.csv') as checklist_file:
        checklist_csv = csv.DictReader(checklist_file)
        for row in checklist_csv:
            title = row['Title'].lower()  # Convert to lowercase for case-insensitive comparison

            # Check if the title is in abe_data.csv titles
            if title in abe_titles:
                # If there is a match, retrieve the corresponding information from abe_data.csv
                writer.writerow({
                    'Title': row['Title'],
                    'Author': row['Author'],
                    'Price': abe_titles[title]['Price']
                })

print(f"Matched data has been written to {output_file_path}.")

