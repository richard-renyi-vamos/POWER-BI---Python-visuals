import matplotlib.pyplot as plt
import numpy as np

# Sample data
category = ['Start Value', 'Positive 1', 'Negative 1', 'Positive 2', 'Negative 2', 'End Value']
values = [100, 40, -20, 60, -30, 150]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Create a waterfall chart
waterfall = ax.waterfall(values, tick_prefix='', open_empty=True)

# Set the x-axis tick labels
ax.set_xticklabels(category, rotation=0)

# Set the y-axis label
ax.set_ylabel('Value')

# Set the title
ax.set_title('Waterfall Chart')

# Adjust the y-axis limits
y_min = min(0, min(values))
y_max = max(0, max(values))
ax.set_ylim(y_min - 10, y_max + 10)

# Show the plot
plt.tight_layout()
plt.show()
