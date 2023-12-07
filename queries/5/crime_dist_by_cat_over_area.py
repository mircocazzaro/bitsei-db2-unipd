import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('5c.csv')

# Extract relevant columns for plotting
areas = df['areaName']
sexual_crimes = df['numSexualCrimes']
property_crimes = df['numPropertyCrimes']
white_collar_crimes = df['numWhiteCollarCrimes']
violent_crimes = df['numViolentCrimes']
public_order_crimes = df['numPublicOrderCrimes']

# Set up the bar positions
bar_width = 0.15
index = range(len(areas))

# Plot the bars
plt.figure(figsize=(20, 10))
plt.bar(index, sexual_crimes, width=bar_width, label='Sexual Crimes')
plt.bar([i + bar_width for i in index], property_crimes, width=bar_width, label='Property Crimes')
plt.bar([i + 2 * bar_width for i in index], white_collar_crimes, width=bar_width, label='White Collar Crimes')
plt.bar([i + 3 * bar_width for i in index], violent_crimes, width=bar_width, label='Violent Crimes')
plt.bar([i + 4 * bar_width for i in index], public_order_crimes, width=bar_width, label='Public Order Crimes')

# Customize the plot
plt.xlabel('Areas')
plt.ylabel('Number of Crimes')
plt.title('Crime Statistics Over Different Areas')
plt.xticks([i + 2 * bar_width for i in index], areas)
plt.legend()


plt.xticks(rotation=80)  # Rotate x-axis labels for better readability
plt.grid(True)
plt.subplots_adjust(bottom=0.24)
# Save the plot as a high-resolution image (1080p)
plt.savefig('crime_dist_by_cat_over_area.png', dpi=300)

