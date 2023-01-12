#You are given a DataFrame that includes the names and ranks of people.
#You need to take a rank as input and output the corresponding name column from the DataFrame as a Series.
#Note that the rank is an integer, so you need to convert the user input to an integer.


import pandas as pd

data = {
   'name': ['James', 'Billy', 'Bob', 'Amy', 'Tom', 'Harry'],
   'rank': [4, 1, 3, 5, 2, 6]
}

df = pd.DataFrame(data, index=data['name'])

user_rank = int(input())

print(df["name"][df["rank"] == user_rank])