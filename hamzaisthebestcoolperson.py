import turtle
turtle.Screen = turtle.bgcolor('pink')
board = turtle.Turtle()

board.forward(100)


board.right(90)
board.forward(100)
board.backward(200)

board.right(90)
board.penup()
board.forward(100)
board.pendown()
board.left(90)
board.forward(200)
turtle.done()