import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'dataset' is the name of your DataFrame in Power BI
# Adjust the column names as per your dataset
df = dataset

# Pivot the DataFrame to create a matrix
matrix_df = df.pivot("Category", "Subcategory", "Measure")

# Create a heatmap using seaborn
plt.figure(figsize=(10, 6))
sns.heatmap(matrix_df, annot=True, fmt=".1f", cmap="YlGnBu", cbar=True)

# Set plot labels and title
plt.title('Measure Matrix')
plt.xlabel('Subcategory')
plt.ylabel('Category')

# Display the plot
plt.show()
