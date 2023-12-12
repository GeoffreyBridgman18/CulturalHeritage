import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('ebay_processed_data.csv')

# Select the top 15 titles based on total price
top_15_titles = df.nlargest(15, 'Total_Price')

# Create a pie chart for the share of market by title (top 15)
plt.figure(figsize=(12, 6))

# Plot the pie chart
plt.subplot(1, 2, 1)
plt.pie(top_15_titles['Total_Price'], labels=top_15_titles['Title'], autopct='%1.1f%%', startangle=140)
plt.title('Share of Market by Title (Top 15)')

# Plot the bar chart for Average Cost by Title
plt.subplot(1, 2, 2)
average_cost_by_title = df.groupby('Title')['Total_Price'].mean().nlargest(15)
average_cost_by_title.plot(kind='bar', color='skyblue')
plt.title('Average Cost by Title')
plt.xlabel('Title')
plt.ylabel('Average Cost')
plt.xticks(rotation=45, ha='right')

# Adjust layout to prevent overlap
plt.tight_layout()

# Save the plots to respective PNG files
plt.savefig('ebay_marketshare_title.png')
plt.savefig('ebay-average_cost_title.png')

# Show the plots
plt.show()






