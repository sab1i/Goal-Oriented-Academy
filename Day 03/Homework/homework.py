import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Castle with Goal-Oriented Academy Logo")

# Create a turtle for drawing the castle
castle_turtle = turtle.Turtle()
castle_turtle.speed(3)
castle_turtle.pensize(3)

# Function to draw a rectangle
def draw_rectangle(turtle, width, height, color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

# Function to draw a square
def draw_square(turtle, size, color):
    draw_rectangle(turtle, size, size, color)

# Function to draw a tower
def draw_tower(turtle, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    draw_rectangle(turtle, width, height, "grey")

    # Draw battlements (small squares on top of the tower)
    turtle.penup()
    turtle.goto(x, y + height)
    turtle.pendown()
    for _ in range(4):
        draw_square(turtle, width / 4, "grey")
        turtle.penup()
        turtle.forward(width / 4)
        turtle.pendown()

# Function to draw the castle
def draw_castle():
    # Draw the main building
    draw_rectangle(castle_turtle, 200, 100, "grey")

    # Draw the left tower
    draw_tower(castle_turtle, -120, 0, 40, 100)

    # Draw the right tower
    draw_tower(castle_turtle, 80, 0, 40, 100)

    # Draw the door
    castle_turtle.penup()
    castle_turtle.goto(-20, 0)
    castle_turtle.pendown()
    draw_rectangle(castle_turtle, 40, 60, "brown")

    # Draw windows
    castle_turtle.penup()
    castle_turtle.goto(-90, -40)
    castle_turtle.pendown()
    draw_square(castle_turtle, 20, "blue")

    castle_turtle.penup()
    castle_turtle.goto(70, -40)
    castle_turtle.pendown()
    draw_square(castle_turtle, 20, "blue")

# Function to draw a star (goal-oriented logo)
def draw_star(turtle, size, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

# Function to draw the goal-oriented academy logo
def draw_logo():
    logo_turtle = turtle.Turtle()
    logo_turtle.speed(3)
    logo_turtle.penup()
    logo_turtle.goto(0, 150)  # Position the logo above the castle
    logo_turtle.pendown()
    draw_star(logo_turtle, 50, "gold")
    logo_turtle.hideturtle()

# Draw the castle
draw_castle()

# Draw the goal-oriented academy logo
draw_logo()

# Hide the castle turtle and finish
castle_turtle.hideturtle()
turtle.done        