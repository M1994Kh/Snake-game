from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,200)
        self.write(f"Score: {self.score}" ,align="center" , font=("Arial",24,"normal") )


    def scoreup(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}" ,align="center" , font=("Arial",24,"normal") )
