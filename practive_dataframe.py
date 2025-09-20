import pandas as pd 
data = {
    "name ":["allice","mohan","rohan"],
    "age" :[21,23,27],
    "city":["mumbai","lucknow","delhi"]
}

df  = pd.DataFrame(data)
print(df.columns)