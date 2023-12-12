import csv
import os

nat_files = {}

# Create 'res' subfolder if it doesn't exist
os.makedirs('res', exist_ok=True)

with open('Artworks.csv') as file:
    processed_csv = csv.DictReader(file)
    for row in processed_csv:
        nationalities_str = row['Nationality']
        nationalities = nationalities_str.split(' ')
        for nat in nationalities:
            if nat not in nat_files:
                # Create 'res' subfolder if it doesn't exist
                os.makedirs('res', exist_ok=True)
                
                # Open CSV file in 'res' subfolder
                file_path = os.path.join('res', f"{nat}.csv")
                nat_file = open(file_path, "w", newline='')
                
                nat_dict_writer = csv.DictWriter(nat_file, fieldnames=processed_csv.fieldnames)
                nat_files[nat] = {"file": nat_file, "nat_dict_writer": nat_dict_writer}
                nat_dict_writer.writeheader()
                
            nat_files[nat]["nat_dict_writer"].writerow(row)

# Close all the created files
for nat_file in nat_files.values():
    nat_file["file"].close()
