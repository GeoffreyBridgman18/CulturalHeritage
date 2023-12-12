import pandas as pd

# Load data from CSV files
abe_data = pd.read_csv('abe_data.csv')
checklist_hogarth_press = pd.read_csv('checklist_hogarth_press.csv')

# Convert titles to lowercase for case-insensitive matching
abe_data['Title_lower'] = abe_data['Title'].str.lower()
checklist_hogarth_press['Title_lower'] = checklist_hogarth_press['Title'].str.lower()

# Merge dataframes based on matching titles
merged_data = pd.merge(
    checklist_hogarth_press,
    abe_data,
    how='inner',
    left_on='Title_lower',
    right_on='Title_lower',
    suffixes=('_hogarth_press', '_abe_data')
)

# Create a new dataframe with the desired columns
result_df = merged_data[['Title_hogarth_press', 'Author_hogarth_press', 'Date', 'Price']]

# Print the new dataframe
print(result_df)

# Save the result to a new CSV file
result_df.to_csv('cleaned_up_abe_data.csv', index=False)
