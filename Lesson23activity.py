import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("white")  # Optional: Set background color

# Create a turtle object
circle_turtle = turtle.Turtle()
circle_turtle.pensize(3)         # Set pen size
circle_turtle.color("blue")      # Set pen color
circle_turtle.speed(2)           # Set drawing speed

# Draw a circle
circle_turtle.circle(100)        # 100 is the radius of the circle

# Keep the window open until clicked
screen.exitonclick()
