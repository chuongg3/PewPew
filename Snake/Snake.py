import pew
import random

pew.init()

snake = [(3, 3), (3,2), (3,1)]

screen = pew.Pix()
dx, dy = 0, 1
blink = True

background = pew.Pix.from_iter(((0, 0, 0, 0, 0, 0, 0, 0),
                                (0, 0, 0, 0, 0, 0, 0, 0),
                                (0, 0, 0, 0, 0, 0, 0, 0),
                                (0, 0, 0, 0, 0, 0, 0, 0),
                                (0, 0, 0, 0, 0, 0, 0, 0),
                                (0, 0, 0, 0, 0, 0, 0, 0),
                                (0, 0, 0, 0, 0, 0, 0, 0),
                                (0, 0, 0, 0, 0, 0, 0, 0),))

food = (random.randint(0, 7), random.randint(0, 7))
speed = 1


while True:
    # Draw the snake
    screen.blit(background)
    for index, element in enumerate(snake):
        if (index != 0):
            screen.pixel(element[0], element[1], 3)
        else:
            screen.pixel(element[0], element[1], 3 if blink == True else 2)
            blink = not blink

    screen.pixel(food[0], food[1], 1)

    # User Input
    keys = pew.keys()
    if keys & pew.K_UP:
        dx = 0
        dy = -1
    elif keys & pew.K_DOWN:
        dx = 0
        dy = 1
    elif keys & pew.K_LEFT:
        dx = -1
        dy = 0
    elif keys & pew.K_RIGHT:
        dx = 1
        dy = 0

    # Update the snake's coordinates
    head = snake[0]
    snake.insert(0, (head[0] + dx, head[1] + dy))
    snake.pop()

    pew.show(screen)
    pew.tick(1/1)