import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('your_csv_file.csv')

# Create the new 'Full Name' column by combining 'First Name' and 'Last Name'
df['Full Name'] = df['First Name'] + ' ' + df['Last Name']

# Save the updated DataFrame back to a CSV file
df.to_csv('updated_csv_file.csv', index=False)