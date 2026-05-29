import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt


# Create the connection engine
engine = create_engine('postgresql://postgres:my password@localhost:5432/ecommerce_analytics')

# join orders and products, and calculate revenue per item
query = """
SELECT 
    p.product_name,
    SUM(o.quantity * p.price) AS total_revenue
FROM orders o
INNER JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name;
"""

#execute the query and store the result in a DataFrame
df = pd.read_sql(query, con=engine)

# Define the size of the window/figure
plt.figure(figsize=(10, 6))

# Create a bar chart: X-axis = product names, Y-axis = total revenue
plt.bar(df['product_name'], df['total_revenue'], color='royalblue')

plt.title('Total Revenue per Product (E-Commerce Analysis)', fontsize=14, fontweight='bold')
plt.xlabel('Product Name', fontsize=12)
plt.ylabel('Revenue in EUR (€)', fontsize=12)

# Rotate product names slightly so they don't overlap each other
plt.xticks(rotation=15)

# Adjust layout automatically to prevent text clipping
plt.tight_layout() 

plt.savefig('product_revenue_chart.png')
plt.show()
