import pandas as pd
import numpy as np
np.random.seed(42)

# Simulate customer dataset
df = pd.DataFrame({
    'customer_id': range(1, 11),
    'age': [25, np.nan, 35, 28, np.nan, 42, 31, np.nan, 27, 38],
    'income': [50000, 65000, np.nan, 48000, 72000, np.nan, 55000, 61000, np.nan, 80000],
    'segment': ['A', 'B', 'A', np.nan, 'C', 'B', np.nan, 'A', 'C', 'B'],
    'churn': [0, 1, 0, 0, 1, 0, 1, 0, 1, 0]
})
print('Shape:', df.shape)
print('Missing values:\n', df.isnull().sum())

# Imputation
df['age'] = df['age'].fillna(df['age'].median())
df['income'] = df['income'].fillna(df['income'].mean())
df['segment'] = df['segment'].fillna(df['segment'].mode()[0])
print('\nAfter imputation - missing values:\n', df.isnull().sum())

# Descriptive stats
print('\nAge stats:', df['age'].describe().round(2))
print('Churn rate:', df['churn'].mean())