import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
import math

# List of transformations and their corresponding probabilities
# transformations = [transformation1, transformation2]
# probabilities = [1/3, 1/3, 1/3]

transformations = []
probabilities = []

num = input("how many transformations would you like to visualize? ")
print("input 2x2 matrix as `a b c d`, then `x y`, where x and y are added after transformation")
print("probabilities will be normalized automatically")
if num == "serp":
    transformations = [
        lambda point: (point[0] * 0.5, point[1] * 0.5),
        lambda point: (point[0] * 0.5 + 0.5, point[1] * 0.5),
        lambda point: (point[0] * 0.5 + 0.25, point[1] * 0.5 + 0.5),
    ]
    probabilities = [1/3, 1/3, 1/3]
elif num == "evantest":
    transformations = [
        lambda point: (point[0] * 1.2, point[1] + 0.1),
        lambda point: (point[0] * .8, point[1] + 0.1),
        lambda point: (point[0] * 1.2, point[1] - 0.1),
        lambda point: (point[0] * .8, point[1] - 0.1),
    ]
    probabilities = [1/4, 1/4, 1/4, 1/4]
elif num == "hex":
    transformations = [
        lambda point: (point[0] * 1.2, point[1]),
        lambda point: (point[0] * -1.2, point[1]),
        lambda point: (point[0] * 1.2, point[1] - 0.1),
        lambda point: (point[0] * 1.1, point[1] - 0.1),
        lambda point: (point[0] * 1.2, point[1] - 0.1),
        lambda point: (point[0] * 1.1, point[1] - 0.1),
    ]
    probabilities = [1/4, 1/4, 1/4, 1/4]
else:
    i = 0
    while i < int(num):
        matrix_nums = input(f"transformation matrix {i+1}: ")
        try:
            a, b, c, d, x, y = (float(n) for n in matrix_nums.split())
            p = input(f"input probability of transformation {i+1}: ")
            transformations.append(lambda point: (a * point[0] + b * point[1] + x, 
                                                c * point[0] + d * point[1] + y))
            probabilities.append(float(p))
            i += 1
        except Exception as e:
            print(e)
            print("try again")
    print(f"read in {int(num)} matrices")

def normalize_list(lst):
    total = sum(lst)
    return [x / total for x in lst]

# Function to apply one of the transformations randomly
def apply_transform(point):
    transformation = np.random.choice(transformations, p=probabilities)
    return transformation(point)

# Generating points of the Sierpinski Triangle
def generate_sierpinski(num_points):
    points = [(0.5, 0.5)]  # Initial point
    for i in range(num_points):
        points_ = []
        for p in points:
            for transform in transformations:
                points_.append(transform(p))
        for p in points_:
            points.append(p)
    return points

# Plotting the generated points
def plot_fractal(num_points):
    ax.clear()  # Clear previous plot
    points = generate_sierpinski(num_points)
    ax.scatter(*zip(*points), s=1, color='blue')
    ax.set_title('Fractal')
    ax.set_aspect('equal', adjustable='box')
    plt.draw()
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.1, 1.1)

# Create a slider for adjusting the number of points
probabilities = normalize_list(probabilities)
fig, ax = plt.subplots()
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)
plt.subplots_adjust(bottom=0.25)
ax_slider = plt.axes([0.1, 0.1, 0.8, 0.03])
slider = Slider(ax_slider, 'Num Points', 0, 7, valinit=5, valstep=1, valfmt='%0.0f')

# Update the plot when the slider value changes
def update(val):
    num_points = int(slider.val)
    plot_fractal(num_points)
    

slider.on_changed(update)

# Initial plot
plot_fractal(5)

plt.show()
