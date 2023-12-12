import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('All_Closed_Businesses_20231101.csv')

# Convert the 'date' column to datetime format, coercing out-of-range dates to NaT
df['LOCATION END DATE'] = pd.to_datetime(df['LOCATION END DATE'], errors='coerce')

# Filter out rows with years before 2018
df = df[df['LOCATION END DATE'].dt.year >= 2018]

df['LOCATION END DATE'] = df['LOCATION END DATE'].dt.strftime('%m/%d/%Y')

# Save the modified DataFrame back to a CSV file
df.to_csv('All_Closed_Businesses_20231101_PARSED.csv', index=False)


