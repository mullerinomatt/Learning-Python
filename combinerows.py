import pandas as pd

# Sample DataFrame
data = {
    'column1': ['A', 'B', 'C'],
    'column2': ['D', 'E', 'F']
}
df = pd.DataFrame(data)

# Concatenate two columns into a new column
df['new_column'] = df['column1'] + df['column2']

print(df)