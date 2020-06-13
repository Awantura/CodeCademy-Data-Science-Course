import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head())

# check which platform is getting the most views
views_per_platform = ad_clicks.groupby('utm_source').user_id.count().reset_index()

# add a new column that determines if an ad was clicked
ad_clicks['is_click'] =  ~ad_clicks.ad_click_timestamp.isnull()

# count the percent of people who clicked on ads from each source
# count the number of clicks for each source
click_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

# pivot the data so that it's more readable
clicks_pivot = click_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
).reset_index()

# add a column with the calculated percentages
clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[True] + clicks_pivot[False]) * 100.0

# analysing an A/B test
# compare the size of each test group
num_people_in_A_B = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(num_people_in_A_B)

# count successful clicks for both groups
click_sum = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

# pivot the data so that it's more readable
click_sum_pivot = click_sum.pivot(
  columns = 'is_click',
  index = 'experimental_group',
  values = 'user_id'
).reset_index()

# compare which group had a bigger succsess rate
# add a column with the calculated percentages
click_sum_pivot['success_rate'] = click_sum_pivot[True] * 100.0 / (click_sum_pivot[True] + click_sum_pivot[False])

print(click_sum_pivot)

# A/B clicks by day
# Group A
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']

a_clicks_by_day = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()

# pivot the data so that it's more readable
a_clicks_by_day_pivot = a_clicks_by_day.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()

# count the percentages
a_clicks_by_day_pivot['click_rate'] = a_clicks_by_day_pivot[True] * 100.0 /(a_clicks_by_day_pivot[True] + a_clicks_by_day_pivot[False])

print(a_clicks_by_day_pivot.head())

# Group B
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

b_clicks_by_day = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()

# pivot the data so that it's more readable
b_clicks_by_day_pivot = b_clicks_by_day.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()

# count the percentages
b_clicks_by_day_pivot['click_rate'] = b_clicks_by_day_pivot[True] * 100.0 /(b_clicks_by_day_pivot[True] + b_clicks_by_day_pivot[False])

print(b_clicks_by_day_pivot.head())

# it's clear that group A had better click rates throughout the week!
