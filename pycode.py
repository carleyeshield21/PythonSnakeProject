# from turtle import Turtle, Screen
# import time
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor('black')
# screen.title('Snacky')
#
#
# start_pos = [(0, 0), (-20,0), (-40,0)]
# shapes = ['turtle', 'square', 'circle']
# segments = []
#
# # Creating square segments with go to starting position and appending it to segments list
# for pos in start_pos:
#     print(start_pos.index(pos))
#     seg = Turtle(shapes[start_pos.index(pos)])
#     # seg = Turtle('turtle')
#     seg.color('cyan')
#     seg.penup()
#     seg.goto(pos)
#     segments.append(seg)
#
# # Moving the squares while game is on
# snake_game_on = True
# while snake_game_on:
#     screen.update()
#     time.sleep(0.1)
#
#     for seg_num in range(len(segments)-1, 0, -1):
#         new_x = segments[seg_num-1].xcor()
#         print(f'new_x ={new_x}')
#         new_y = segments[seg_num-1].ycor()
#         print(f'new_y={new_y}')
#         segments[seg_num].goto(new_x,new_y)
#     segments[0].forward(20)
#     segments[0].left(90)
#
# screen.exitonclick()

for new_x in range(10,290,10):
    new_y = new_x
    print(new_x, new_y)