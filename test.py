import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plot the data
for i in range(len(x)):
    plt.plot(x[i], y[i], 'o', label=x[0] if i == 0 else '')  # Plot each point individually, only label the first point

# Add labels to the plot
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Add a title
plt.title('Sample Plot')

# Add legend
plt.legend()

# Display the plot
plt.show()
