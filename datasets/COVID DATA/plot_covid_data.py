import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('sorted_los_angeles_covid_data.csv')

# Assuming you have a 'date' column and a 'confirmed' column
# If your column names are different, replace them accordingly

# Convert 'date' column to datetime format (in case it's not already)
df['Last_Update'] = pd.to_datetime(df['Last_Update'], format='mixed')

# Create a line plot
plt.figure(figsize=(10, 5))
plt.plot(df['Last_Update'], df['Confirmed'], marker='o', linestyle='-')

# Add title and labels
plt.title('Confirmed Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Save the plot as a high-resolution image (e.g., PNG with 300 DPI)
plt.tight_layout()
plt.savefig('confirmed_cases_plot.png', dpi=300)