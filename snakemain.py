from turtle import Screen
from snake2 import Snake
import time, random
from food import Food
from scoreboard2_with_score_data import Scoreboard

# Python code with text file
# file = open('my_text.txt')
# contents = file.read()
# print(contents)
# file.close()

# OR this code so the program also closes the text when we exit the program without using the file.close() function
# with open('my_text.txt', mode='a') as file:
#     file.write('\nAppend this')
#     # contents = file.read()
#     # print(contents)

# with open('snake_score_data.txt', mode='a') as file:
#     file.write('0')

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
# Using the tracer method to stop the animation of the movement and we can use the update method
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,'w')
screen.onkey(snake.down,'s')
screen.onkey(snake.left,'a')
screen.onkey(snake.right, 'd')
screen.onkey(snake.quit, 'q')

food.randomize()

# random_x = random.randint(-280, 280)
# random_y = random.randint(-280, 280)
# print(random_x, random_y)
# food.goto(random_x, random_y)

# Moving the squares while game is on
t = 0.059
# t = 0.3
snake_game_on = True
while snake_game_on:
    screen.update()
    time.sleep(t)
    snake.move()

    if snake.head.distance(food) < 15:
        print('mon, mon, mon')
        # food.randomize()
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        print(random_x, random_y)
        food.goto(random_x, random_y)
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_score()
        snake.clear_segments()
        # snake_game_on = False
        # score.update_score()
        # score.game_over()

    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         snake_game_on = False
    #         score.tail_hit()
    #     # print(segment)

# OR by using the slice method
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.clear_segments()
            # score.tail_hit()
            # score.reset_score()
            # snake_game_on = False
            # snake.clear_segments()

screen.exitonclick()

    # start_pos = [(0, 0), (-20,0), (-40,0)]

    # segments = []

    # Creating square segments with go to starting position and appending it to segments list
    # for pos in start_pos:
    #     seg = Turtle('circle')
    #     seg.color('cyan')
    #     seg.penup()
    #     seg.goto(pos)
    #     segments.append(seg)

    # screen.update()
    # screen.listen()
    # screen.onkey(snake.up,'Up')
    # screen.onkey(snake.down,'Down')
    # screen.onkey(snake.left,'Left')
    # screen.onkey(snake.right, 'Right')

    # for seg_num in range(len(segments)-1, 0, -1):
    #     new_x = segments[seg_num-1].xcor()
    #     print(f'new_x ={new_x}')
    #     new_y = segments[seg_num-1].ycor()
    #     print(f'new_y={new_y}')
    #     segments[seg_num].goto(new_x,new_y)
    # segments[0].forward(20)
    # segments[0].left(90)

    # for seg_num in range(start=2, stop=0, step=-1) => we must first move the last square to the position where the
    # previous square is until it reaches the first square, in this case where there is 3 squares, the start position
    # is the last square which has an index of 2, the stop position is the first square which has an index of 0,
    # the step is -1 because it goes backwards

    # for segs in segments:
    #     segs.forward(20)
        # screen.update()
        # time.sleep(1)

# seg_1 =Turtle('square')
# seg_1.color('white')
# seg_2 =Turtle('square')
# seg_2.color('white')
# seg_2.goto(-20,0)
# seg_3 =Turtle('square')
# seg_3.color('white')
# seg_3.goto(-40,0)

# NOTE: In randomizing the location of the food created, we can create a function in the food.py file as an object
# oriented programming and calling it out whenever the conditional if statement is satisfied, or we can put it
# directly under the condition

