import pandas as pd

# Sales dataset
sales = pd.DataFrame({
    'region': ['North','South','North','East','South','East','North'],
    'product': ['A','B','A','C','A','B','C'],
    'revenue': [12000, 8500, 15000, 9200, 7800, 11000, 13500],
    'units': [120, 85, 150, 92, 78, 110, 135]
})

# GroupBy aggregation
region_stats = sales.groupby('region').agg(
    total_revenue=('revenue', 'sum'),
    avg_units=('units', 'mean'),
    product_count=('product', 'nunique')
).round(2)
print('Region Statistics:')
print(region_stats)

# Pivot table
pivot = sales.pivot_table(values='revenue', index='region', columns='product', aggfunc='sum', fill_value=0)
print('\nPivot Table (Revenue):')
print(pivot)

# SQL-style merge
region_meta = pd.DataFrame({'region': ['North','South','East'], 'manager': ['Alice','Bob','Carol']})
merged = sales.merge(region_meta, on='region', how='left')
print('\nMerged with manager info:')
print(merged[['region','product','revenue','manager']].head())