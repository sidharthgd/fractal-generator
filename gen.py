import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

# Define the three affine transformations for the Sierpinski Triangle
def transformation1(point):
    x, y = point
    return x * 0.5, y * 0.5

def transformation2(point):
    x, y = point
    return x * 0.5 + 0.5, y * 0.5

def transformation3(point):
    x, y = point
    return x * 0.5 + 0.25, y * 0.5 + 0.5

def square1(point):
    x, y = point
    return x / 3, y / 3

def square2(point):
    x, y = point
    return x / 3 + 1/3, y / 3

def square3(point):
    x, y = point
    return x / 3, y / 3 + 1/3

def square4(point):
    x, y = point
    return x / 3 + 2/3, y / 3

def square5(point):
    x, y = point
    return x / 3, y / 3 + 2/3

def square6(point):
    x, y = point
    return x / 3 + 1/3, y / 3 + 2/3

def square7(point):
    x, y = point
    return x / 3 + 2/3, y / 3 + 1/3

def square8(point):
    x, y = point
    return x / 3 + 2/3, y / 3 + 2/3

def transformation4(point):
    x, y = point
    return x / 4 + 0.5, y / 4 + 0.5

def transformation5(point):
    x, y = point
    return x * 0.75, y - 0.1

def transformation6(point):
    x, y = point
    return x / 2 + 0.5, y / 2

def transformation7(point):
    x, y = point
    return x * 1.01, y + 0.01

def transformation8(point):
    x, y = point
    return x + 0.01, y * 1.01

# List of transformations and their corresponding probabilities
# transformations = [transformation1, transformation2, transformation3]
# probabilities = [1/4, 1/2, 1/4]

transformations = [square1, square2, square3, square4, square5, square6, square7, square8]
probabilities = [1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8]


# Function to apply one of the transformations randomly
def apply_transform(point):
    transformation = np.random.choice(transformations, p=probabilities)
    return transformation(point)

# Generating points of the Sierpinski Triangle
def generate_sierpinski(num_points):
    points = [(0.0, 0.0)]  # Initial point
    for i in range(num_points):
        points.append(apply_transform(points[-1]))
    return points

# Plotting the generated points
def plot_sierpinski(num_points):
    ax.clear()  # Clear previous plot
    points = generate_sierpinski(num_points)
    ax.scatter(*zip(*points), s=1, color='blue')
    ax.set_title('Sierpinski Triangle')
    ax.set_aspect('equal', adjustable='box')
    plt.draw()

# Create a slider for adjusting the number of points
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
ax_slider = plt.axes([0.1, 0.1, 0.8, 0.03])
slider = Slider(ax_slider, 'Num Points', 0, 20000, valinit=1, valstep=250, valfmt='%0.0f')

# Update the plot when the slider value changes
def update(val):
    num_points = int(slider.val)
    plot_sierpinski(num_points)

slider.on_changed(update)

# Initial plot
plot_sierpinski(10000)

plt.show()
