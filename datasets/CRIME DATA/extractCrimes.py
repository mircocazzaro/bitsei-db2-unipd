import pandas as pd

# Replace these with the paths to your input CSV files
input_files = ['Crime_Data_from_2020_to_Present_1.csv', 'Crime_Data_from_2020_to_Present_2.csv', 'Crime_Data_from_2020_to_Present_3.csv']
output_file = 'output_file.csv'

# Create an empty dictionary to store unique codes and descriptions
unique_codes = {}

# Iterate through each input CSV file
for input_file in input_files:
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Iterate through the rows in the DataFrame
    for index, row in df.iterrows():
        code = row['Crm Cd']
        description = row['Crm Cd Desc']

        # Check if the code is not in the dictionary
        if code not in unique_codes:
            unique_codes[code] = description

# Create a new DataFrame from the unique codes and descriptions
unique_df = pd.DataFrame(list(unique_codes.items()), columns=['Code', 'Description'])

# Write the unique data to a new CSV file
unique_df.to_csv(output_file, index=False)

print("Unique codes and descriptions have been extracted and saved to", output_file)
