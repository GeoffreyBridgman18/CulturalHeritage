import csv

nat_files = {}
with open('Artworks.csv') as file:
    processed_csv = csv.DictReader(file)
    for row in processed_csv:
        nationalities_str = row['Nationality']
        nationalities = nationalities_str.split(' ')
        for nat in nationalities:
clean_nat_match = regex.match(nat)
print(nat)
if clean_nat_match is Name:
            continuenat = 

            nat_file = open(f"{nat}.csv", "w")
            nat_dict_writer = csv.DictWriter(nat_file, fieldnames=processed_csv.fieldnames)
            nat_files[nat] = {"file": nat_file, "nat_dict_writer": nat_dict_writer}
            nat_dict_writer.writeheader()
            nat_dict_writer.writerow(row)