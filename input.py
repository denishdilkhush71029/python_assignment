import matplotlib.pyplot as plt

# Example data
months = [1, 2, 3, 4, 5]
profits = [1000, 1500, 2000, 2500, 3000]

# Create the line plot
plt.plot(months, profits)

# Set the required axis labels
plt.xlabel('Month Number')
plt.ylabel('Profit in dollar')

# Display the plot
plt.show()   