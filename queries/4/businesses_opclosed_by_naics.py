import pandas as pd
import matplotlib.pyplot as plt


# Read CSV file into a DataFrame
dfa = pd.read_csv('4a.csv')
dfb = pd.read_csv('4b.csv')

# Merge the DataFrames on the 'sigla' column
merged_df = pd.merge(dfa, dfb, on='naicsDesc')

#print(merged_df.head(10))

# Plotting
fig, ax = plt.subplots(figsize=(30, 20))
bar_width = 0.4
bar_positions = range(len(merged_df))

# Plotting bars for each file
ax.bar(bar_positions, merged_df['openedBusinesses'], width=bar_width, label='Opened Businesses', color="green", edgecolor='black')
ax.bar([pos + bar_width for pos in bar_positions], merged_df['closedBusinesses'], width=bar_width, label='Closed Businesses', color="red",edgecolor='black')

# Set labels and title
ax.set_xticks([pos + bar_width for pos in bar_positions])
ax.set_xticklabels(merged_df['naicsDesc'])
ax.set_xlabel('North American Industry Classification System')
ax.set_ylabel('Number of Businesses')
ax.set_title('Number of Businesses Closed for Each NAICS')

# Display legend
ax.legend()

plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.grid(True)
plt.subplots_adjust(bottom=0.25)
plt.savefig("businesses_opclosed_by_naics.png", dpi=400)

