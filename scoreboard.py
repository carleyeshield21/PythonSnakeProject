from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.update_score()
        # self.write(f'score: {self.score}', align='center', font=('Roboto', 20, 'normal'))
        self.hideturtle()

    def update_score(self):
        self.write(f'score: {self.score}', align='center', font=('Roboto', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        # self.write(f'score: {self.score}', align='center', font=('Roboto', 20, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write('Wall hit! Game Over!', align='center', font=('ComicSans', 20, 'normal'))

    def tail_hit(self):
        self.goto(0, 0)
        self.write('Tail hit! Game Over!', align='center', font=('ComicSans', 20, 'normal'))
