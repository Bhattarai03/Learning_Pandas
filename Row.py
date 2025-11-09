# head(n)  for displaying the first n no. of rows in the dataset
# head()    for displaying the top 5 no .of rows in the dataset
# tail(n)   for displaying the last n no. of rows in the dataset
# tail()    for displaying the bottom 5 no .of rows in the datase

import pandas as pd 
'For reading Csv file'
df=pd.read_csv("random_fitness_dataset.csv",encoding="latin1")

print("Display first 10 rows:")
print(df.head(10))
print("Display last 10 rows:")
print(df.tail(10))