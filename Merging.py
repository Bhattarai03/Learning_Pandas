# Merging two or more rows of different data sets

import pandas as pd
df_Customer=pd.DataFrame({
    "customer":[1,2,3],
    "Name":["Raman","Suresh","Kalmesh"]
})

df_Order=pd.DataFrame({
    "customer":[1,2,4],
    "OrderAmount":[250,564,456]

})

df_merged=pd.merge(df_Customer,df_Order,on="customer",how="inner")
'inner for showing the value whose key are matched'
print(df_merged)

df_merged=pd.merge(df_Customer,df_Order,on="customer",how="outer")
'outer for showing all the value in the dataframes'
print(df_merged)

df_merged=pd.merge(df_Customer,df_Order,on="customer",how="left")
'In a left merge, all rows from the left DataFrame are kept and pandas matches rows from the right DataFrame wherever possible based on the key column.'
print(df_merged)

df_merged=pd.merge(df_Customer,df_Order,on="customer",how="right")
'A right merge (or right join) keeps all rows from the right DataFrame and matches data from the left DataFrame wherever possible.'
print(df_merged)