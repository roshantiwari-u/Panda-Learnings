import pandas as pd
employees = pd.DataFrame({
    "employe id":[1,2,3],
    "name":["alice","bob","charlie"],
    "department id":[10,20,30]

})

department=pd.DataFrame({
    "department id":[10,20,40],
    "department name":["hr","engineering","marketing"]
})

# Inner join

print(pd.merge(employees,department,on="department id"))

# right join
print(pd.merge(employees,department,on="department id",how="right"))

# left join
print(pd.merge(employees,department,on="department id",how="left"))