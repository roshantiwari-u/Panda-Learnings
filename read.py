import pandas as pd 
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

# we do eda in the given data set
#print(df.head()) # in given head(10) are giveing first 10 rows
#print(df.tail()) # in given tail(10) are giving last 10 rows
#print(df.shape) # (rows,columns)
#print(df.info()) # columns information.types,non nulls 
#print(df.describe()) # stats for numeric data

#print(df.columns) # list of column names
#print(df.iloc[2,1]) # iloc used indices of rows and columns 2,1 means 2nd rows and 1 column by their indices 
#fir=df[(df["day"]=="Sun") & (df["size"]<4)]
#print(fir)
print(df)
#print(df.isnull())
#print(df.iloc[5,3])

















