import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data
# Assuming the CSV file has columns: 'Product', 'Category', 'Quantity', 'Price'
data = {
    "Product": ["A", "B", "C", "D", "E"],
    "Category": ["Electronics", "Electronics", "Clothing", "Clothing", "Food"],
    "Quantity": [10, 15, 20, 10, 30],
    "Price": [200, 150, 50, 40, 10],
}
df = pd.DataFrame(data)

# Step 2: Add a new column 'Total Sales'
df['Total Sales'] = df['Quantity'] * df['Price']

# Step 3: Group data by 'Category' and calculate total sales
category_sales = df.groupby('Category')['Total Sales'].sum()

# Step 4: Visualize the results
plt.figure(figsize=(8, 6))
category_sales.plot(kind='bar', color='skyblue', edgecolor='black')

# Customize the plot
plt.title('Total Sales by Category', fontsize=16)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
