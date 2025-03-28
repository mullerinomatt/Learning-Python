>>> import pandas as pd
>>> data = {'Info': ['apple,red', 'banana,yellow', 'grape,purple']}
>>> df = pd.DataFrame(data)
>>>
>>> df[['Fruit', 'Color']] = df['Info'].str.split(',', expand=True)
>>> print(df)
            Info   Fruit   Color
0      apple,red   apple     red
1  banana,yellow  banana  yellow
2   grape,purple   grape  purple