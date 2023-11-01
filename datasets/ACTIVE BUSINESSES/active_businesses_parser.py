import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('Listing_of_Active_Businesses.csv')

# Convert the 'date' column to datetime format
df['LOCATION START DATE'] = pd.to_datetime(df['LOCATION START DATE'])

# Filter out rows with years before 2020
df = df[df['LOCATION START DATE'].dt.year >= 2020]

# Save the modified DataFrame back to a CSV file
df.to_csv('Listing_of_Active_Businesses_parsed.csv', index=False)