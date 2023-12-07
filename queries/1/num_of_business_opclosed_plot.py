import pandas as pd
import matplotlib.pyplot as plt


# Read CSV file into a DataFrame
dfb = pd.read_csv('1b.csv')
dfc = pd.read_csv('1c.csv')

merged_df = pd.merge(dfb, dfc, on='period')

# Plotting
plt.figure(figsize=(16, 9))  # Set the figure size to 1080p resolution (16:9 aspect ratio)
plt.plot(merged_df['period'], merged_df['openedBusinesses'], marker='o', linestyle='-', linewidth=2.5, color="green", label='Opened Businesses')  # Adjust linewidth as needed
plt.plot(merged_df['period'], merged_df['closedBusinesses'], marker='o', linestyle='-', linewidth=2.5, color="red", label='Closed Businesses')  # Adjust linewidth as needed
plt.title('Number of Opened/Closed Businesses Over Time')
plt.xlabel('Period')
plt.ylabel('Number of Businesses')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)
plt.legend()

# Save the plot as a high-resolution image (1080p)
plt.savefig('num_of_businesses_opclosed_plot.png', dpi=300)
