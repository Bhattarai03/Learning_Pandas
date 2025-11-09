
import pandas as pd


data={
    "Name":["Raman","Suraj","Peshal","Saroj"],
    "Age":[12,23,34,45],
    "City":["Nagpur","Itahari","Sonapur","Biratnagar"],
    "Salary":[45000,34000,45000,567]

}

df=pd.DataFrame(data)
print(df)
# For inserting the new column and value in it
df["Bonus"]=df["Salary"]*0.1

print(df)

# For inserting new column and its value in the specific index
df.insert(2,"Ph_no",[9845673,34864946,4856373,236465347])
print(df)

# For updating the value in specific cell
df.loc[1,"Ph_no"]=9867564534
print(df)

# For updating all the value in a specific column
df["Salary"]=df["Salary"]*1.5
print(df)

# For removing the specific row or column in the datasets
df.drop(columns=["Bonus","Ph_no"],inplace=True)
print(df)