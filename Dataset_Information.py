'''
1- columns,rows ?
2- about data type
3- missing data ?
'''


'''
info()
method

1-number of rows and columns
2-column name
3=data type(int,float)
4-non null counts
5-memory usage of the dataframe

'''
import pandas as pd


data={
    "Name":["Raman","Suraj","Peshal","Saroj"],
    "Age":[12,23,34,45],
    "City":["Nagpur","Itahari","Sonapur","Biratnagar"]

}





df=pd.DataFrame(data)
print(df)


print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)