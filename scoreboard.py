from turtle import Turtle

Y_LOCATION = 275
ALIGN = "Center"
FONT = ("Ariel", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("score.txt", "r") as score_file:
            content = score_file.read()
            self.high_score = int(content)
        self.level = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.goto(0, Y_LOCATION)
        self.write(f"Level: {self.level} High Score: {self.high_score}", False, ALIGN, FONT)

    def increase_level(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGN, FONT)
        if self.level > self.high_score:
            self.high_score = self.level
            with open("score.txt", "w") as score_file:
                score_file.write(f"{self.level}")

    def reset_game(self):
        self.level = 0
        self.update()




