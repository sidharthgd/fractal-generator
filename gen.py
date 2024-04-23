import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
import math
import sys

if (len(sys.argv) > 1):
    sys.stdin = open(sys.argv[1], 'r')

transformations = []
probabilities = []
starting_points = [(0, 0)]
x_min = -0.1
x_max = 1.1
y_min = -0.1
y_max = 1.1

print("transformation is of form")
print()
print("|a b u|")
print("|c d v|")
print("|0 0 1|")
print()
print("such that A[x, y, 1] = [ax + by + u, cx + dy + v, 1]")
print()
num = input("number of transformations to visualize ")
print("input as 'a b c d u v (p)' ")
print("probabilities will be normalized automatically")
i = 0
while i < int(num):
    matrix_nums = input(f"transformation matrix {i+1}: ")
    try:
        a, b, c, d, u, v = (float(n) for n in matrix_nums.split())
        transformations.append(lambda point, a=a, b=b, c=c, d=d, u=u, v=v: (a * point[0] + b * point[1] + u, 
                                            c * point[0] + d * point[1] + v))
        i += 1
        print(f"{a} {b} {c} {d} {u} {v} ")
    except Exception as e:
        print(e)
        print("try again")
print(f"\nread in {int(num)} matrices")
custom_points = input("custom starting points? y/n ")
custom_points = (custom_points == "y")
if custom_points:
    starting_points.clear()
    npoints = int(input("how many points? "))
    for i in range(npoints):
        p = input(f"point {i}")
        x, y = (float(n) for n in p.split())
        starting_points.append((x, y))
    print(f"read in {npoints} points")
custom_dimensions = input("custom starting points? y/n ")
custom_dimensions = (custom_dimensions == "y")
if custom_dimensions:
    x_min = float(input("lower bound for x "))
    x_max = float(input("upper bound for x "))
    y_min = float(input("lower bound for y "))
    y_max = float(input("upper bound for y "))
    print(f"read in custom probabilities {x_min} {x_max} {y_min} {y_max}")

def normalize_list(lst):
    total = sum(lst)
    return [x / total for x in lst]

# Generating points of the Sierpinski Triangle
def generate_sierpinski(num_points):
    points = starting_points.copy()
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
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    plt.draw()

# Create a slider for adjusting the number of points
probabilities = normalize_list(probabilities)
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
ax_slider = plt.axes([0.1, 0.1, 0.8, 0.03])
max_iterations = int(28 / len(transformations))
if len(transformations) > 5:
    max_iterations = 5
slider = Slider(ax_slider, 'Num Points', 0, max_iterations, valinit=min(max_iterations - 2, 7), valstep=1, valfmt='%0.0f')

# Update the plot when the slider value changes
def update(val):
    num_points = int(slider.val)
    plot_fractal(num_points)
    

slider.on_changed(update)

# Initial plot
plot_fractal(min(max_iterations - 2, 7))

plt.show()