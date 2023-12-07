import pandas as pd
import matplotlib.pyplot as plt


# Read CSV file into a DataFrame
dfb = pd.read_csv('2b.csv')
dfc = pd.read_csv('2c.csv')

merged_df = pd.merge(dfb, dfc, on='periodLabel')

# Plotting
plt.figure(figsize=(28, 17))  # Set the figure size to 1080p resolution (16:9 aspect ratio)
plt.plot(merged_df['periodLabel'], merged_df['openedRatio'], marker='o', linestyle='-', linewidth=2.5, color="green", label='Opened Businesses Ratios')  # Adjust linewidth as needed
plt.plot(merged_df['periodLabel'], merged_df['closedRatio'], marker='o', linestyle='-', linewidth=2.5, color="red", label='Closed Businesses Ratios')  # Adjust linewidth as needed
plt.title('Number of Opened/Closed Businesses Ratios Over Time')
plt.xlabel('Period')
plt.ylabel('Businesses/Days')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)
plt.legend()

# Save the plot as a high-resolution image (1080p)
plt.savefig('num_of_business_opclosedRatios_plot.png', dpi=300)
