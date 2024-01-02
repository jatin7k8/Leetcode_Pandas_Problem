import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    buyA = orders.loc[orders['product_name'] == 'A', 'customer_id']
    buyB = orders.loc[orders['product_name'] == 'B', 'customer_id']
    buyC = orders.loc[orders['product_name'] == 'C', 'customer_id']

    condA = customers['customer_id'].isin(buyA)
    condB = customers['customer_id'].isin(buyB)
    condC = ~customers['customer_id'].isin(buyC)

    df = customers[condA & condB & condC]

    return df[['customer_id','customer_name']]

data = [[1, 'Daniel'], [2, 'Diana'], [3, 'Elizabeth'], [4, 'Jhon']]
customers = pd.DataFrame(data, columns=['customer_id', 'customer_name']).astype({'customer_id':'Int64', 'customer_name':'object'})
data = [[10, 1, 'A'], [20, 1, 'B'], [30, 1, 'D'], [40, 1, 'C'], [50, 2, 'A'], [60, 3, 'A'], [70, 3, 'B'], [80, 3, 'D'], [90, 4, 'C']]
orders = pd.DataFrame(data, columns=['order_id', 'customer_id', 'product_name']).astype({'order_id':'Int64', 'customer_id':'Int64', 'product_name':'object'})

result = find_customers(customers, orders)
print(result)