import pandas as pd
df=pd.DataFrame({
    "name":["roshan","raj"],
    "age":[19,20]
})

df1= pd.DataFrame({
    "name ":["alice","bob"],
    "score":[87,90]
})

print(pd.concat([df,df1],axis=1))