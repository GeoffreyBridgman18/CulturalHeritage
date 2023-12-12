import csv

# Define the base URL and initial entry number
base_url = "https://www.abebooks.com/servlet/SearchResults?yrl=1917&recentlyadded=all&prevpage={}&xpod=off&bx=off&bi=0&bsi={}&sortby=0&yrh=1941&pn=Hogarth+Press&ds=50"

# Number of entries
num_entries = 50  # You can change this to the desired number of entries

# Create a list to store the data
data = []

# Manually add the first URL
first_url = "https://www.abebooks.com/servlet/SearchResults?bi=0&bx=off&cm_sp=SearchF-_-Advs-_-Result&ds=50&pn=hogarth%20press&recentlyadded=all&rollup=on&sortby=0&sts=t&xdesc=off&xpod=off&yrh=1941&yrl=1917"
data.append([first_url])

# Create the CSV data
for entry_number in range(2, num_entries + 1):
    prev_page = entry_number - 1
    bsi_value = (entry_number - 1) * 50
    url = base_url.format(prev_page, bsi_value)
    data.append([url])

# Write the data to a CSV file
csv_file_path = "url_generator.csv"

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{csv_file_path}' has been created.")

