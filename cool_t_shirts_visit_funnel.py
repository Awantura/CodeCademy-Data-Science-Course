import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

# explore the DataFrames
#print(visits.head())
#print(cart.head())
#print(checkout.head())
#print(purchase.head())

# VISIT/CART
visits_to_cart = pd.merge(visits, cart, how='left')
#print(visits_to_cart.head())

# number of users that visited the site
visits_to_cart_total = len(visits_to_cart)

# number of users that did not add a t-shirt to the cart (out of the ones that visited the site, of course)
null_cart_times = len(visits_to_cart[visits_to_cart.cart_time.isnull()])
print('Null_cart_times: ' + str(null_cart_times))

# calculate and print the visit/cart exit rate
visits_to_cart_exit_rate = float(null_cart_times) / visits_to_cart_total

print('Exit rate from visit to cart: ' + '{:.2%}'.format(round(visits_to_cart_exit_rate, 2)))

# CART/CHECKOUT
cart_to_checkout = pd.merge(cart, checkout, how='left')
#print(cart_to_checkout.head())

# number of users that added to cart
cart_to_checkout_total = len(cart_to_checkout)

# numbers of users that clicked 'checkout' (out of the ones that added to the cart)
null_checkout_times = len(cart_to_checkout[cart_to_checkout.checkout_time.isnull()])

# calculate and print the visit/cart exit rate
cart_to_checkout_exit_rate = float(null_checkout_times) / cart_to_checkout_total

print('Exit rate from cart to checkout: ' + '{:.2%}'.format(round(cart_to_checkout_exit_rate, 2)))

# CHECKOUT/PURCHASE
checkout_to_purchase = pd.merge(checkout, purchase, how='left')

# number of users that clicked 'checkout'
checkout_to_purchase_total = len(checkout_to_purchase)

# number of users that didn't purchase the product (out of the ones that clicked 'checkout')
null_purchase_times = len(checkout_to_purchase[checkout_to_purchase.purchase_time.isnull()])

# calculate and print the checkout/purchase exit rate
cart_to_checkout_exit_rate = float(null_purchase_times) / checkout_to_purchase_total

print('Exit rate from checkout to purchase: ' + '{:.2%}'.format(round(cart_to_checkout_exit_rate, 2)))

# merge all information into a funnnel
all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')

# calculate the average time from initial visit to purchase
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

print(all_data.time_to_purchase)
print(all_data.head())
