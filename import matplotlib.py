import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperature = [22, 24, 19, 23, 25, 27, 26]  # Example temperatures in °C

# Create line plot
plt.plot(days, temperature, marker='o', linestyle='-', linewidth=2)

# Add labels and title
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Variation Over a Week')

# Optional: Add grid and adjust layout
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
