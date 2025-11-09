import pandas as pd


data={
    "Name":["Raman","Suraj","Peshal","Saroj"],
    "Age":[12,23,34,45],
    "City":["Nagpur","Itahari","Sonapur","Biratnagar"]

}

df=pd.DataFrame(data)
print(df)

# df.to_csv("Student.csv")

# For removing indexing
df.to_csv("Student.Update.csv", index=False)

'For saving into excel file, give command:pip install pandas openpyxl'
 

df.to_excel("Student.Update.json", index=False)


'For saving into json file'
df.to_json("Student.Update.json", index=False)
