import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('los_angeles_covid_data.csv')


# Sort the DataFrame by the 'date' column
df = df.sort_values(by='Last_Update')

# Save the modified DataFrame back to a CSV file
df.to_csv('sorted_los_angeles_covid_data.csv', index=False)