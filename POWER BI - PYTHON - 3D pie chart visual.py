import matplotlib.pyplot as plt

# Data
labels = ['Category A', 'Category B', 'Category C']
sizes = [30, 40, 30]  # Dummy data for illustration

# Create a pie chart
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.set_aspect('equal')

# Show plot
plt.savefig('3d_pie_chart.png')  # Save the chart as an image
