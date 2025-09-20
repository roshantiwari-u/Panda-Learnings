import pandas as pd 
data = {
    "Name":["alice","bob","charlie"],
    "math":[85,78,92],
    "science":[90,82,89],
    "english":[88,85,94]

}
df=pd.DataFrame(data)
df1=df.melt(id_vars=["Name"], value_vars=["math", "science", "english"], var_name="Subject", value_name="Score")
print(df1)