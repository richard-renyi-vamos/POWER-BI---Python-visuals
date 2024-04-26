import matplotlib.pyplot as plt

# Sample data (replace this with your data)
countries = ['USA', 'Canada', 'Mexico']
values = [100, 200, 150]

# Plot the map chart
plt.figure(figsize=(10, 6))
plt.bar(countries, values, color='skyblue')
plt.xlabel('Country')
plt.ylabel('Value')
plt.title('Map Chart')
plt.show()
