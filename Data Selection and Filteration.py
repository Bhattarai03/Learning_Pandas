'''
1-select specific column
2-filter rows
3-combine multiple conditons
'''

import pandas as pd


data={
    "Name":["Raman","Suraj","Peshal","Saroj"],
    "Age":[12,23,34,45],
    "City":["Nagpur","Itahari","Sonapur","Biratnagar"]

}

df=pd.DataFrame(data)
print(df)

# For selecting single columns
print(df["Name"])

# For selecting multiple columns
print(df[["Name","Age"]])

# For filtering single row
print(df[df["Age"] >18])

# For filtering multiple row
print(df[(df["Age"]>18) & (df["Age"]<26)])
print(df[(df["Age"]>18) | (df["Age"]<26)])



 
