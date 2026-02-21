import turtle

# for canvas
turtle.Screen().bgcolor("Orange")

sc = turtle.screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle window")

# turtle for creating object
board = turtle.Turtle()

# fro square
for i in range(4):
    board.forward(100)
    board.left(90)
    i = i+1