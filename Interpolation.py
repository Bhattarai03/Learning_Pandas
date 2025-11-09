# Inserting the estimated value in the missing place
import pandas as pd

data={
    "Name":["Raman","Suraj","Peshal","Saroj"],
    "Age":[12,None,34,45],
    "City":["Nagpur","Itahari","Sonapur","Biratnagar"],
    "Ph_no":[98,96,None,92]


}

df=pd.DataFrame(data)
print(df)

'''
Types of method
linear,polynomial,time and many more ......
'''
df.interpolate(method="linear",axis=0,inplace=True)


print(df)