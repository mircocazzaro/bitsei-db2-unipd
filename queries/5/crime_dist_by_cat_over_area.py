import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
bar_width = 0.5
index = range(len(areas))

# Plot the stacked bars
plt.figure(figsize=(20, 10)) 
plt.bar(index, property_crimes, width=bar_width, label='Property Crimes')
plt.bar(index, violent_crimes, width=bar_width, label='Violent Crimes', bottom=property_crimes)
plt.bar(index, public_order_crimes, width=bar_width, label='Public Order Crimes', bottom=violent_crimes + property_crimes)
plt.bar(index, white_collar_crimes, width=bar_width, label='White Collar Crimes', bottom=property_crimes + public_order_crimes + violent_crimes)
plt.bar(index, sexual_crimes, width=bar_width, label='Sexual Crimes', bottom=property_crimes + public_order_crimes + violent_crimes + white_collar_crimes)

# Plot the line plot interpolating the top of each column
#top_interpolated = np.sum([sexual_crimes, property_crimes, white_collar_crimes, violent_crimes, public_order_crimes], axis=0)
#plt.plot(index, top_interpolated, color='black', marker='o', linestyle='-', linewidth=2, markersize=8, label='Top Interpolated')

# Interpolate the top of each column for a smoother line
top_interpolated = np.sum([sexual_crimes, property_crimes, white_collar_crimes, violent_crimes, public_order_crimes], axis=0)
top_interpolated_smooth = np.interp(np.linspace(0, len(index)-1, 100), index, top_interpolated)

# Plot the smoothed line
plt.plot(np.linspace(0, len(index)-1, 100), top_interpolated_smooth, color='black', linewidth=2, label='Top Interpolated')



# Customize the plot
plt.xlabel('areas')
plt.ylabel('Number of Crimes')
plt.title('Stacked Crime Statistics Over Different areas')
plt.xticks(index, areas, rotation=70, ha='right')  # Rotate labels and set alignment
plt.legend()
plt.grid(True)
plt.subplots_adjust(bottom=0.25)
plt.savefig('crime_dist_by_cat_over_area.png', dpi=300)