import pandas as pd
import matplotlib.pyplot as plt


# Read CSV file into a DataFrame
df = pd.read_csv('1d.csv')

# Plotting
plt.figure(figsize=(16, 9))  # Set the figure size to 1080p resolution (16:9 aspect ratio)
plt.plot(df['period'], df['crimeEvents'], marker='o', linestyle='-', linewidth=2.5, color='orange')  # Adjust linewidth as needed
plt.title('Number of Crime Events Over Time')
plt.xlabel('Period')
plt.ylabel('Number of Crime Events')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)

# Save the plot as a high-resolution image (1080p)
plt.savefig('num_of_crimeEvents_plot.png', dpi=300)
