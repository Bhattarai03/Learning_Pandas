'''
Vertically(Row wise)
Horizontally (Column wise)
'''
import pandas as pd
df_Customer=pd.DataFrame({
    "customer":[1,2,3],
    "Name":["Raman","Suresh","Kalmesh"]
})

df_Order=pd.DataFrame({
    "customer":[4,5,6],
    "Name":["Bimal","Samyok","Roshan"]

})
pd_concate=pd.concat([df_Order,df_Customer],axis=0,ignore_index=True)
# ignore_index=True tells pandas to ignore the existing row indexes from the original DataFrames or Series and create a new continuous index (0, 1, 2, …) for the result.
print(pd_concate)

df_update=pd.DataFrame({
    "Salary":[234,345,456],
    "No_of_item":[2,3,6]

})

pd_con=pd.concat([df_Customer,df_update],axis=1,ignore_index=True)
print(pd_con)