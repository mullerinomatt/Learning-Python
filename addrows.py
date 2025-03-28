import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}
df = pd.DataFrame(data)

# Custom function to modify each row
def modify_row(row):
    return row['A'] + row['B']

# Apply function to each row and create a new column
df['C'] = df.apply(modify_row, axis=1)

print(df)