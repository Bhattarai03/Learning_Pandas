import pandas as pd


data={
    "Name":["Raman","Raj","Peshal","Saroj"],
    "Age":[12,23,34,None],
    "City":["Nagpur","Itahari","Kuwait","Biratnagar"]

}

df=pd.DataFrame(data)
print(df)
print(df.isnull())

# For knowing the no of null value in the dataset
print(df.isnull().sum())


# For removing the row containing null value 
# df.dropna(axis=0,inplace=True)
# print(df)

# For removing the column containing null value 
# df.dropna(axis=1 ,inplace=True)
# print(df)

# For inserting a default value in the missing value
df["Age"].fillna(df["Age"].mean(),inplace=True)
print(df)