from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        self.positions = [(0 , 0), (-20 , 0 ) , (-40 , 0)]
        for part in self.positions:
            segment = Turtle()
            segment.penup()
            segment.color("white")
            segment.shape("circle")
            self.segments.append(segment)
            segment.goto(part) 


    def move(self):
        for i in range (1 , len(self.segments)):
            self.segments[-i].goto(self.positions[-i-1])
    

    def prize(self):
        for i in range (1 , len(self.segments)):
            self.segments[-i].goto(self.positions[-i-1])
        segment = Turtle()
        segment.penup()
        segment.color("white")
        segment.shape("circle")
        self.segments.append(segment)
        segment.goto(self.positions[-1])   
        # self.head.forward(20)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)


    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)


    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)



