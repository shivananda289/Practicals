import numpy as np
import matplotlib.pyplot as plt

# Ellipse parameters
a = 5   # Semi-major axis
b = 3   # Semi-minor axis

# Calculate distance from center to focus (c = √(a² - b²))
c = np.sqrt(a**2 - b**2)

# Angle values from 0 to 2π
theta = np.linspace(0, 2 * np.pi, 1000)

# Parametric equations of ellipse centered at origin
x = a * np.cos(theta)
y = b * np.sin(theta)

# Shift the ellipse so that the Sun (focus) is at (0,0)
x_shifted = x - c

# Plot the orbit
plt.figure(figsize=(8, 6))
plt.plot(x_shifted, y, label='Planet Orbit (Ellipse)')
plt.plot(0, 0, 'yo', label='Focus (Sun)', markersize=10)
plt.title('Elliptical Orbit Simulation')
plt.xlabel('X Position (AU)')
plt.ylabel('Y Position (AU)')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()
