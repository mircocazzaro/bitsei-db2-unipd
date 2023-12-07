import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV
df = pd.read_csv('5a.csv')

# Plotting the pie chart with both percentage and absolute number labels
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(df['numOfCrimeEvents'], labels=df['crimeCategory'], autopct=lambda p: '{:.1f}%\n({:.0f})'.format(p, p * sum(df['numOfCrimeEvents']) / 100), startangle=140)

# Adjusting the appearance of the labels
for text, autotext in zip(texts, autotexts):
    text.set_size(10)
    autotext.set_size(8)

ax.set_title('Crime Distribution by Category')
# Save the plot to an image file
plt.savefig('crime_dist_by_cat.png', dpi=300)  # Adjust dpi for better resolution