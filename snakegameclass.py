import turtle
from random import randint

class SnakeGame:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.game = True
        self.scoreboard = Scoreboard()
        self.gameovertext = Gameovertext()
        self.timer = 0.05
        self.frenzy = False

    def update(self):
        self.snake.update_coordinates()
        self.check_colision()
        self.snake.move()
        self.scoreboard.printself()

    def score_up(self):
        self.snake.add()
        self.scoreboard.increase_score()

    def check_colision(self):
        for i in self.snake.body[1:]:
            if self.snake.headpos == i.pos():
                #print("Colidiu consigo mesmo")
                self.game = False

        if self.snake.head.distance(self.fruit) < 15:
            #print("Comeu uma fruta")
            self.score_up()
            self.fruit.position_fruit()

        if self.snake.headpos[0] < -280 or self.snake.headpos[0] > 280:
            #print("Colidiu na parede")
            self.game = False

        if self.snake.headpos[1] < -280 or self.snake.headpos[1] > 280:
            #print("Colidiu na parede")
            self.game = False


class Snake:
    def __init__(self):
        self.body = []
        self.size = 3
        self.head = None
        self.headpos = (0, 0)
        self.body_coordinates = None
        self.direction = "horizontal"
        self.create_snake()

    def create_square(self):
        square = turtle.Turtle()
        square.shape("square")
        square.color("white")
        square.shapesize()
        square.penup()
        return square

    def add(self):
        square = self.create_square()
        last_square_pos = list(self.body[-1].pos())
        if self.direction == "horizontal":
            last_square_pos[0] -= 20

        elif self.direction == "vertical":
            last_square_pos[1] -= 20

        last_square_pos = tuple(last_square_pos)

        square.goto(last_square_pos)
        self.body.append(square)
        self.size += 1

    def create_snake(self):
        self.body = [self.create_square() for i in range(self.size)]
        self.headpos = self.body[0].pos()
        self.body[1].goto((self.headpos[0] - 20, self.headpos[1]))
        self.body[2].goto((self.headpos[0] - 40, self.headpos[1]))
        self.head = self.body[0]

    def turn(self):

        def right():
            if self.direction == "vertical":
                self.head.setheading(0)
                self.direction = "horizontal"
                return

        def left():
            if self.direction == "vertical":
                self.head.setheading(180)
                self.direction = "horizontal"
                return

        def up():
            if self.direction == "horizontal":
                self.head.setheading(90)
                self.direction = "vertical"
                return

        def down():
            if self.direction == "horizontal":
                self.head.setheading(270)
                self.direction = "vertical"
                return

        turtle.listen()
        turtle.onkeypress(up, 'w')
        turtle.onkeypress(down, 's')
        turtle.onkeypress(right, 'd')
        turtle.onkeypress(left, 'a')

    def move(self):
        self.move_body(self.size - 1)
        self.turn()

    def move_body(self, index):
        actual_square = self.body[index]
        actual_square_pos = tuple([round(i) for i in actual_square.pos()])

        if actual_square_pos == self.headpos:
            previous_head_pos = actual_square_pos
            self.head.forward(20)
            self.update_coordinates()
            return previous_head_pos

        else:
            actual_square.goto(self.move_body(index - 1))
            return actual_square_pos

    def update_coordinates(self):
        coordinates = self.head.pos()
        coordinates = list(coordinates)
        coordinates[0] = round(coordinates[0])
        coordinates[1] = round(coordinates[1])
        self.headpos = tuple(coordinates)
        self.body_coordinates = [turtle.pos() for turtle in self.body]


class Fruit(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(0.5, 0.5)
        self.position_fruit()
        self.coordinates = self.pos()

    def position_fruit(self):
        self.goto(20 * randint(-14, 14), 20 * randint(-14, 14))

    def refresh_fruit(self):
        self.position_fruit()


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 255)
        self.hideturtle()

    def printself(self):
        self.clear()

        self.write(f"Score: {self.score}", False, align="center", font=("Jetbrains Mono", 24, "normal"))

    def increase_score(self):
        self.score += 1


class Gameovertext(Scoreboard):
    def __init__(self):
        super().__init__()
        self.goto(0, 0)

    def printself(self):
        self.clear()
        self.write(f"Game Over", False, align="center", font=("Jetbrains Mono", 24, "normal"))
