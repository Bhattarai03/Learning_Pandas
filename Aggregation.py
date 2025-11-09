import pandas as pd


data={
    "Name":["Raman","Suraj","Peshal","Saroj"],
    "Age":[12,23,34,23],
    "City":["Nagpur","Itahari","Sonapur","Biratnagar"],
    "Salary":[45000,34000,45000,567]

}

df=pd.DataFrame(data)
print(df)

print(df["Age"].mean())


group=df.groupby("Age")["Salary"].mean()
print(group)


# Grouping multiple column
grouped=df.groupby(["Age","Name"])["Salary"].mean()
print(grouped)