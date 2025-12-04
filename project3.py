'''
Zuzia Bownik
Project 3
My scene is just a simple house, but now generalized to draw multiple houses easily.
'''

# loads the Turtle graphics module, which is a built-in library in Python
import turtle
import math


def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen


def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_square(t, size, fill_color=None):
    """Draw a square with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    """Draw an equilateral triangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    """Draw a circle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()


def draw_polygon(t, sides, size, fill_color=None):
    """Draw a regular polygon with given number of sides"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()


def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    """Draw a curved line using small line segments"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()

    segment_length = length / segments
    original_heading = t.heading()

    for i in range(segments):
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)

    t.setheading(original_heading)

    if fill_color:
        t.end_fill()


def jump_to(t, x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw_house(t, x, y, size, wall_color, roof_color, door_color, window_color):
    """
    Draws a house at position (x, y) with customizable size and colors.
    """
    # House base
    jump_to(t, x, y)
    draw_square(t, size, wall_color)

    # Roof
    jump_to(t, x, y)
    draw_triangle(t, size, roof_color)

    # Door
    door_width = size * 0.2
    door_height = size * 0.5
    jump_to(t, x + size * 0.4, y - door_height)
    draw_rectangle(t, door_width, door_height, door_color)

    # Windows
    window_size = size * 0.2
    window_offset = size * 0.1

    # Left window
    jump_to(t, x + window_offset, y - window_offset - window_size)
    draw_square(t, window_size, window_color)

    # Right window
    jump_to(t, x + size - window_size - window_offset, y - window_offset - window_size)
    draw_square(t, window_size, window_color)



def draw_scene(t):
    """Draw a colorful scene with multiple houses"""
    screen = t.getscreen()
    screen.bgcolor("skyblue")

    # Sun
    jump_to(t, -250, 150)
    draw_circle(t, 50, "yellow")

    # Grass
    jump_to(t, -400, -100)
    t.setheading(0)
    draw_rectangle(t, 800, 400, "lightgreen")

    # Houses (different sizes, colors, positions)
    draw_house(t, x=-150, y=0, size=150, wall_color="orange", roof_color="red", door_color="brown", window_color="lightblue")
    draw_house(t, x=100, y=-50, size=100, wall_color="pink", roof_color="purple", door_color="navy", window_color="white")
    draw_house(t, x=-350, y=-30, size=120, wall_color="yellow", roof_color="darkred", door_color="chocolate", window_color="skyblue")


# Main function

def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()


# Run program

if __name__ == "__main__":
    main()
