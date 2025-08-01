import pandas as pd
import os

#create a sample DataFrame with column names
data = {'Name' : ['alice', 'bob', 'joy'],
        'Age': [21,22,32],
        'City': [ 'jaipur', 'goa', 'pune']
        }

df = pd.DataFrame(data)

## Adding new roe to df for v2
new_row_loc = {'Name': "GF1", 'Age': '20', 'City': 'city1' }
df.loc[len(df.index)] = new_row_loc

## adding new row to df for v3
new_row_loc2 = {'Name': "GF2", 'Age': '30', 'City': 'city2' }
df.loc[len(df.index)] = new_row_loc2


## 3nsure the 'data' directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir , exist_ok=True)

# define the file path
file_path = os.path.join(data_dir , ' sample_data.csv')

# save the dataframe to a csv file , icluding coulmn names
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")
