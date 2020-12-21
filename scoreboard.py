from turtle import Turtle

Y_LOCATION = 275
ALIGN = "Center"
FONT = ("Ariel", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("white")
        self.penup()
        self.goto(0, Y_LOCATION)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Level: {self.level}", False, ALIGN, FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGN, FONT)




