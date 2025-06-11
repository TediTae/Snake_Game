from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def  __init__(self):

        self.snake_squares = []
        self.create_snake()
        self.head = self.snake_squares[0]

    def create_snake(self):
        for positions in STARTING_POSITION:
            self.add_segment(positions)

    def add_segment(self, positions):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(positions)
        self.snake_squares.append(new_turtle)

    def extend(self):
        self.add_segment(self.snake_squares[-1].position())

    def move(self):

        for seg_num in range(len(self.snake_squares) - 1, 0, -1):
            new_x = self.snake_squares[seg_num - 1].xcor()
            new_y = self.snake_squares[seg_num - 1].ycor()
            self.snake_squares[seg_num].goto(new_x, new_y)
        self.snake_squares[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
