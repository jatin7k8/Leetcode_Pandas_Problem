import pandas as pd

def most_frequently_products(customers: pd.DataFrame, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    customers = orders.groupby(['customer_id', 'product_id']).agg(no_order = ('product_id','count')).reset_index()
    customers.sort_values(by = ['customer_id', 'no_order'], ascending= [True,False], inplace = True)
    customers['most_frequen_no_order'] = customers.groupby('customer_id')['no_order'].transform('first')
    data = customers[customers['no_order'] == customers['most_frequen_no_order']]
    result  = data.merge(products, on = 'product_id', how = 'left')
    return result[['customer_id','product_id', 'product_name']]


data = [[1, 'Alice'], [2, 'Bob'], [3, 'Tom'], [4, 'Jerry'], [5, 'John']]
customers = pd.DataFrame(data, columns=['customer_id', 'name']).astype({'customer_id':'Int64', 'name':'object'})
data = [[1, '2020-07-31', 1, 1], [2, '2020-7-30', 2, 2], [3, '2020-08-29', 3, 3], [4, '2020-07-29', 4, 1], [5, '2020-06-10', 1, 2], [6, '2020-08-01', 2, 1], [7, '2020-08-01', 3, 3], [8, '2020-08-03', 1, 2], [9, '2020-08-07', 2, 3], [10, '2020-07-15', 1, 2]]
orders = pd.DataFrame(data, columns=['order_id', 'order_date', 'customer_id', 'product_id']).astype({'order_id':'Int64', 'order_date':'datetime64[ns]', 'customer_id':'Int64', 'product_id':'Int64'})
data = [[1, 'keyboard', 120], [2, 'mouse', 80], [3, 'screen', 600], [4, 'hard disk', 450]]
products = pd.DataFrame(data, columns=['product_id', 'product_name', 'price']).astype({'product_id':'Int64', 'product_name':'object', 'price':'Int64'})

ans = most_frequently_products(customers, orders,products)
print(ans)