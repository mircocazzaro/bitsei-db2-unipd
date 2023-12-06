import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files
file1 = "2020.csv"
file2 = "2021.csv"
file3 = "2022.csv"

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)

# Merge the DataFrames on the 'sigla' column
merged_df = pd.merge(df1, df2, on='sigla')
merged_df = pd.merge(merged_df, df3, on='sigla')

#print(merged_df.head(10))

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.25
bar_positions = range(len(merged_df))

# Plotting bars for each file
ax.bar(bar_positions, merged_df['numBusinesses_x'], width=bar_width, label='2020')
ax.bar([pos + bar_width for pos in bar_positions], merged_df['numBusinesses_y'], width=bar_width, label='2021')
ax.bar([pos + 2 * bar_width for pos in bar_positions], merged_df['numBusinesses'], width=bar_width, label='2022')

# Set labels and title
ax.set_xticks([pos + bar_width for pos in bar_positions])
ax.set_xticklabels(merged_df['sigla'])
ax.set_xlabel('Area')
ax.set_ylabel('Number of Businesses Opened')
ax.set_title('Number of Businesses Opened for Each Area')

# Display legend
ax.legend()

#plt.savefig("businesses_opened_by_year.svg")
# Show the plot
plt.tight_layout()
plt.show()
