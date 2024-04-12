import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
import math
import sys

sys.stdin = open('sierpinski.txt', 'r')

transformations = []
probabilities = []

print("transformation is of form")
print()
print("|a b u|")
print("|c d v|")
print("|0 0 1|")
print()
print("such that A[x, y, 1] = [ax + by + u, cx + dy + v, 1]")
print()
num = input("number of transformations to visualize ")
custom_probs = input("custom probabilities y/n ")
custom_probs = (custom_probs == "y")
print("input as 'a b c d u v (p)' ")
print("probabilities will be normalized automatically")
i = 0
while i < int(num):
    matrix_nums = input(f"transformation matrix {i+1}: ")
    try:
        a, b, c, d, u, v = (float(n) for n in matrix_nums.split())
        transformations.append(lambda point, a=a, b=b, c=c, d=d, u=u, v=v: (a * point[0] + b * point[1] + u, 
                                            c * point[0] + d * point[1] + v))
        p = 1
        if custom_probs:
            p = int(matrix_nums[-1])
        probabilities.append(p)
        i += 1
        print(f"{a} {b} {c} {d} {u} {v} {p} ")
    except Exception as e:
        print(e)
        print("try again")
print(f"\nread in {int(num)} matrices")

def normalize_list(lst):
    print(lst)
    total = sum(lst)
    return [x / total for x in lst]

# Generating points of the Sierpinski Triangle
def generate_sierpinski(num_points):
    points = [(0, 0)]
    # points = [(0.5, 0),(-0.5, 0),(0.25980762113, 0.25),(-0.25980762113, 0.25),(0.25980762113, -0.25),(-0.25980762113, -0.25)]
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
    # ax.set_xlim(-1.1, 1.1)
    # ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.1, 1.1)
    plt.draw()

# Create a slider for adjusting the number of points
probabilities = normalize_list(probabilities)
fig, ax = plt.subplots()
# ax.set_xlim(-1.1, 1.1)
# ax.set_ylim(-1.1, 1.1)
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
