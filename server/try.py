import matplotlib.pyplot as plt

# Sample data
categories = ['Tempo', 'Acousticness', 'Sound']
values = [120, 0.9, 18]

# Create a bar graph
plt.bar(categories, values, color=['blue', 'green', 'red'])

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Basic Bar Graph')

# Display the graph
plt.show()