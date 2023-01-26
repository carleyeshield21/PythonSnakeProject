from turtle import Turtle
import random
START_POS = [(0, 0), (-20,0), (-40,0)]
SHAPES = ['turtle', 'square', 'circle']
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in START_POS:
            self.add_segment(pos)
            # seg = Turtle(SHAPES[START_POS.index(pos)])
            # # seg = Turtle('triangle')
            # seg.color('cyan')
            # seg.penup()
            # seg.goto(pos)
            # self.segments.append(seg)

    def add_segment(self, pos):
        for pos in  START_POS:
            seg = Turtle(SHAPES[random.randint(0,2)])
        # seg = Turtle('square')
        # seg = Turtle('triangle')
        seg.color('cyan')
        seg.penup()
        seg.goto(pos)
        self.segments.append(seg)

    def extend(self):
        # any of these 3 codes will extend the snake
        # self.add_segment(self.segments[-1].position())
        # self.add_segment(self.segments[-1].pos())
        self.add_segment(self.segments[-1])

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            # print(f'new_x ={new_x}')
            new_y = self.segments[seg_num - 1].ycor()
            # print(f'new_y={new_y}')
            self.segments[seg_num].goto(new_x, new_y)
            # print(f'seg_num = {seg_num}')
        self.segments[0].forward(MOVE_DISTANCE)
        # self.segments[0].left(90)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    def quit(self):
        pass

    def clear_segments(self):
        for seg in self.segments:
            seg.goto(0,0)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    # def up(self):
    #     if self.head.heading() != DOWN:
    #         self.head.setheading(UP)
    # def down(self):
    #     if self.head.heading() != UP:
    #         self.head.setheading(DOWN)
    # def left(self):
    #     if self.head.heading() != RIGHT:
    #         self.head.setheading(LEFT)
    # def right(self):
    #     if self.head.heading() != LEFT:
    #         self.head.setheading(RIGHT)