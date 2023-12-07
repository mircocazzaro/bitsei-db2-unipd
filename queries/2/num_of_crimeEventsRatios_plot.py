import pandas as pd
import matplotlib.pyplot as plt


# Read CSV file into a DataFrame
df = pd.read_csv('2d.csv')

# Plotting
plt.figure(figsize=(28, 17))  # Set the figure size to 1080p resolution (16:9 aspect ratio)
plt.plot(df['periodLabel'], df['crimeEventsRatio'], marker='o', linestyle='-', linewidth=2.5, color="orange")  # Adjust linewidth as needed
plt.title('Crime Events Ratios Over Time')
plt.xlabel('Period')
plt.ylabel('Crime Events/Days')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)

# Save the plot as a high-resolution image (1080p)
plt.savefig('num_of_crimeEventsRatios_plot.png', dpi=400)
