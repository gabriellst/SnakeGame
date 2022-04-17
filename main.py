from snakegameclass import *
from time import sleep

turtle.tracer(0)
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Gabriel's Snake Game")

game = SnakeGame()

while True:
    sleep(game.timer)
    screen.update()
    game.update()

    if not game.game:
        game.gameovertext.printself()
        break

screen.exitonclick()
