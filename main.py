from turtle import Screen
import time
from Snake import Snake
from Food import Food
from Scoreboard import Score



screen = Screen()
screen.setup(width=640 , height=480)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")


snake = Snake()
food = Food()
score = Score()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right ,"Right")
t = 0.5

game_is_on = True
while game_is_on:
    snake.positions.append(snake.head.position())
    positions2 = list()
    for i in range (len(snake.segments)):
        pos1 = snake.segments[i].position()
        xpos2 = pos1[0]
        ypos2 = pos1[1]
        if pos1[0] > 320:
            xpos2 = pos1[0] - 640
        if pos1[0] < -320:
            xpos2 = pos1[0] + 640
        if pos1[1] > 240:
            ypos2 = pos1[1] - 480
        if pos1[1] < -240:
            ypos2 = pos1[1] + 480
        snake.segments[i].goto(xpos2 , ypos2)
        if snake.segments[i].position() not in positions2:
            positions2.append(snake.segments[i].position())
    positions = positions2
    if snake.head.distance(food) <15:
        food.refresh()
        score.scoreup()
        snake.prize()
        t *= 0.9
    else:
        snake.move()
    screen.update()
    snake.head.forward(20)
    for segment in snake.segments[2:]:
        if snake.head.distance(segment) <5:
            score.clear()
            score.write(f"Game Over" ,align="center" , font=("Arial",24,"normal") )
            time.sleep(5)
            game_is_on = False

    score
    time.sleep(t)

screen.exitonclick()
