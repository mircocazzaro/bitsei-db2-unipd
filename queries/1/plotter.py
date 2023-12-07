import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('1a.csv')

# Plotting
fig, ax = plt.subplots(figsize=(30, 12))
bar_width = 0.33
bar_positions = range(len(df))

# Plotting bars for each file
ax.bar(bar_positions, df['numOfCovidCases'], width=bar_width, label='No. of covid cases')
ax.bar([pos + bar_width for pos in bar_positions], df['numOfDeaths'], width=bar_width, label='No. of deaths')

# Set labels and title
ax.set_xticks([pos + bar_width for pos in bar_positions])
ax.set_xticklabels(df['period'])
ax.set_xlabel('Period')
ax.set_ylabel('People')
ax.set_title('Number of COVID cases and deaths grouped by month and year')

# Display legend
ax.legend()
# Save the plot as an image file (e.g., PNG)
plt.savefig('1a.png')