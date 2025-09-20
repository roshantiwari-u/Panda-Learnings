import pandas as pd 
data = [["harry",90],["shubham",87],["jack",89]]
#print(pd.DataFrame(data,columns=["NAME","MARKS"]))
data1 = {"a":[10,20,30],
         "b":[40,50,60]
}
#print(pd.DataFrame(data1,))

import numpy as np 
arr = np.array([[10,20],[30,40]])
print(pd.DataFrame(arr,columns=["A","B"]))

