import matplotlib.pyplot as plt

# Read data from the file
with open('test.txt', 'r') as file:
    data = [line.strip().split(', ') for line in file]

# Extract columns
x_values = [float(row[0]) for row in data]
y1_values = [float(row[1]) for row in data]
y2_values = [float(row[2]) for row in data]
y3_values = [float(row[3]) for row in data]

# Create the graph
plt.figure(figsize=(10, 6))
plt.plot(x_values, y1_values, label='Column 1')
plt.plot(x_values, y2_values, label='Column 2')
plt.plot(x_values, y3_values, label='Column 3')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph from test.txt')

# Add a legend
plt.legend()

# Show the graph
plt.show()
