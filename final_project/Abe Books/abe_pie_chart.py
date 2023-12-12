import pandas as pd
import matplotlib.pyplot as plt

# Load the processed data
df = pd.read_csv('abe_clean_data.csv')

# Clean and convert the 'Price' column to numeric
df['Price'] = df['Price'].replace('[^\d.]', '', regex=True).astype(float)

# Sort the DataFrame by Price in descending order
df_sorted_by_price = df.sort_values(by='Price', ascending=False)

# Extract the top 15 titles
top_15_titles = df_sorted_by_price.head(15)

# Plotting "Share of AbeBook Market by Title"
plt.figure(figsize=(10, 6))
plt.pie(top_15_titles['Price'], labels=top_15_titles['Title'], autopct='%1.1f%%', startangle=140)
plt.title('Share of AbeBook Market by Title')
plt.savefig('abebook_market_title.png')  # Save the chart
plt.show()

# Plotting "Share of AbeBook Market by Author" (limited to top 15 authors)
author_group = df.groupby('Author')['Price'].sum().reset_index()
author_group_sorted = author_group.sort_values(by='Price', ascending=False)

top_15_authors = author_group_sorted.head(15)  # Extract the top 15 authors

plt.figure(figsize=(10, 6))
plt.pie(top_15_authors['Price'], labels=top_15_authors['Author'], autopct='%1.1f%%', startangle=140)
plt.title('Share of AbeBook Market by Author (Top 15)')
plt.savefig('abebook_market_by_author.png')  # Save the chart
plt.show()

# Plotting "Average Cost of Top 20 Titles"
top_20_titles = df_sorted_by_price.head(20)  # Extract the top 20 titles
plt.figure(figsize=(12, 6))
plt.bar(top_20_titles['Title'], top_20_titles['Price'], color='skyblue')
plt.title('Average Cost of Top 20 Titles')
plt.xlabel('Title')
plt.ylabel('Average Cost')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('abe_books_average_cost_titles.png')  # Save the chart
plt.show()

# Plotting "Average Cost by Top 20 Authors"
top_20_authors = author_group_sorted.head(20)  # Extract the top 20 authors
plt.figure(figsize=(12, 6))
plt.bar(top_20_authors['Author'], top_20_authors['Price'], color='salmon')
plt.title('Average Cost by Top 20 Authors')
plt.xlabel('Author')
plt.ylabel('Average Cost')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('abebooks_average_cost_authors.png')  # Save the chart
plt.show()
