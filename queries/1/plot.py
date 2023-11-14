import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file into a DataFrame
df = pd.read_csv('query-result.csv')

# Convert the 'timestamp' column to datetime format with a specific format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%dT%H:%M:%S')

# Plot the data
plt.plot(df['date'], df['happenedCrimes'])
plt.title('Your Plot Title')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.show()