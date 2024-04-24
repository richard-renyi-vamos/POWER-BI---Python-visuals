import matplotlib.pyplot as plt
import pandas as pd

# Sample data (replace this with your actual data)
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Revenue': [100000, 120000, 150000, 180000, 200000],
    'Expenses': [60000, 65000, 70000, 75000, 80000]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Plotting the line chart
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Revenue'], marker='o', label='Revenue')
plt.plot(df['Year'], df['Expenses'], marker='o', label='Expenses')
plt.xlabel('Year')
plt.ylabel('Amount ($)')
plt.title('Revenue and Expenses Over Time')
plt.legend()
plt.grid(True)

# Save the plot as an image file
plt.savefig('line_chart.png')

# Close the plot to free up memory
plt.close()

# Output the file path of the saved image
print("Line chart saved as 'line_chart.png'")
