#pd.merge() is used to merge two dataframes based on a common column or index.
#pd.merge(df1,df2, on = "column_name", how = (type)"inner/outer/left/right", indicator = True/False)

import pandas as pd

data_custam = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4],
    "CustomerName": ["John Doe", "Anna Smith", "Peter Brown", "Linda White"],
    "CarModel": ["Toyota", "Honda", "Ford", "BMW"],
})
data_orders = pd.DataFrame({
    "OrderID": [101, 102, 103, 104],
    "CustomerID": [1, 5, 3, 6],
    "OrderAmount": [25000, 30000, 15000, 20000],
})

merge_data= pd.merge(data_custam, data_orders, on="CustomerID", how="inner", ) 
#Inner join can be used to merge common data in customers ID (1,3) 
print("Merged DataFrame:")
print(merge_data)
merge_data= pd.merge(data_custam, data_orders, on="CustomerID", how="outer", )
#Outer join can be used to merge all the data in both dataframes
merge_data= pd.merge(data_custam, data_orders, on="CustomerID", how="left", )
#left join can be used to left dataframe(data_custam) and with comman data in right dataframe(data_orders)
merge_data= pd.merge(data_custam, data_orders, on="CustomerID", how="right", )
#right join can be used to right dataframe(data_orders) and with comman data in left dataframe(data_custam)