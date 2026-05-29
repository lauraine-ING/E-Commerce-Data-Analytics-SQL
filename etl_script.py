import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv("weekly_sales.csv")

print("--- 1. EXTRACT: Original Data ---")
print(df)

df['quantity'] = df['quantity'].fillna(1)

df = df[df['quantity'] > 0]

df['quantity'] = df['quantity'].astype(int)

print("\n--- 2. TRANSFORM: Cleaned Data ---")
print(df)

print("\n--- 3. LOAD: Injecting data into PostgreSQL ---")

# Create a connection engine to PostgreSQL
engine = create_engine('postgresql://postgres:my_password@localhost:5432/ecommerce_analytics')

# Insert the Pandas DataFrame directly into the existing 'orders' table
df.to_sql('orders', con=engine, if_exists='append', index=False)

print("Data successfully loaded into PostgreSQL!")
