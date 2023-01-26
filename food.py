from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('triangle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        # self.randomize()
        # random_x = random.randint(-280, 280)
        # random_y = random.randint(-280, 280)
        # self.goto(random_x, random_y)

    def randomize(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 270)
        self.goto(random_x, random_y)

# turtle_food = Food()
#
# screen.exitonclick()

# from turtle import Turtle, Screen
# screen = Screen()
# screen.bgcolor('black')
#
# coordinates = [(0,0), (-20,0), (-40,0)]
# parts = []
# shapes = ['arrow', 'circle', 'turtle']
#
# for coord in coordinates:
#     # print(coord)
#     # print(coordinates.index(coord))
#     # print(shapes[coordinates.index(coord)])
#     # part = Turtle('triangle')
#     part = Turtle(shapes[coordinates.index(coord)])
#     part.color('cyan')
#     part.goto(coord)
#     parts.append(part)
#
#
# for xy in range(len(coordinates)-1, 0, -1):
#     print(xy)
#
#
# screen.exitonclick()

# ######################################################
# Sample Codes on Inheritance of Classes

# class Hayup:
#     def __init__(self):
#         self.canine_teeth = 4
#
#     def bite(self):
#         print('Sweetie')
#
# class Pusa(Hayup):
#     def __init__(self):
#         super().__init__()
#
#     def eat(self):
#         print('Kakain na')
#
#     def bite(self):
#         super().bite()
#         print('May pusang kumakain')
#
# orange = Pusa()
# orange.eat()
# orange.bite()
# print(orange.canine_teeth)