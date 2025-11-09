# Sorting data
'''
df.sort_values[by="Column Name",True/False , inplace=True]
'''

import pandas as pd
data={
    "Name":["Raman","Bhuwan","Nitesh","Subodh"],
    "Age":[23,45,34,54],
    "Salary":[10000,20000,30000,40000]
}

df=pd.DataFrame(data)
df.sort_values(by=["Name"],ascending=True,inplace=True)
print(df)


# Sorting multiple rows
df.sort_values(by=["Name","Age"],ascending=[True,True],inplace=True)