import os
import pandas as pd

# Set the directory path where your CSV files are stored
directory_path = '../../../PROJECT/zzzz_COVID-19/csse_covid_19_data/csse_covid_19_daily_reports'

# Initialize an empty DataFrame to store the filtered data
filtered_data = pd.DataFrame()

# Iterate through each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".csv"):
        # Load the CSV file into a DataFrame
        df = pd.read_csv(os.path.join(directory_path, filename))
        
        # Check if 'city' column exists in the DataFrame
        if 'Admin2' in df.columns:
            # Filter rows where 'city' is 'Los Angeles'
            los_angeles_data = df[df['Admin2'] == 'Los Angeles']
            
            # Concatenate the filtered data to the main DataFrame
            filtered_data = pd.concat([filtered_data, los_angeles_data], ignore_index=True)

# Save the filtered data to a new CSV file
filtered_data.to_csv('los_angeles_covid_data.csv', index=False)