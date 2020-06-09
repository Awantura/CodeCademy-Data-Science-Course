import codecademylib
import pandas as pd

# load the data
inventory = pd.read_csv('inventory.csv')

# inspect the first 10 rows
print(inventory.head(10))

# first 10 items come from Staten Island
staten_island = inventory[:10]

# review the products sold at Staten Island
product_request = staten_island['product_description']

# a customer requests seeds in Brooklyn
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]

# add a column to check if a given item is in stock
inventory['in_stock'] = inventory.apply(lambda row: True if row['quantity'] > 0 else False, axis = 1)

# add a column to calculate total value of each product in the inventory
inventory['total_value'] = inventory['price'] * inventory['quantity']

# add a complete description of each product in the catalogue
combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis = 1)

print(inventory)
