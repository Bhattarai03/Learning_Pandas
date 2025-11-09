import pandas as pd 
'For reading Csv file'
df=pd.read_csv("random_fitness_dataset.csv",encoding="latin1")
'For reading json file'
# df=pd.read_json("Path of the file")
'For reading excel file'
# df=pd.read_excel("Path of the file")

print(df)

