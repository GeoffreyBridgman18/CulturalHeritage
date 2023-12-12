import json
import os

nat_files = {}

# Create 'res' subfolder if it doesn't exist
os.makedirs('res', exist_ok=True)

with open('Artworks.json') as file:
    artworks_data = json.load(file)
    for row in artworks_data:
        nationalities_str = row.get('Nationality', '')
        nationalities = nationalities_str.split(' ')
        for nat in nationalities:
            if nat not in nat_files:
                # Create 'res' subfolder if it doesn't exist
                os.makedirs('res', exist_ok=True)
                
                # Open JSON file in 'res' subfolder
                file_path = os.path.join('res', f"{nat}.json")
                nat_file = open(file_path, "w")
                
                nat_dict_writer = json.dump([row], nat_file, indent=2)
                nat_files[nat] = {"file": nat_file, "nat_dict_writer": nat_dict_writer}
                
            else:
                # Append to existing JSON file
                nat_files[nat]["nat_dict_writer"].write(',\n')
                json.dump(row, nat_files[nat]["file"], indent=2)
                
# Close all the created files
for nat_file in nat_files.values():
    nat_file["file"].close()
