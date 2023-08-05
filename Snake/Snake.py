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

end = pew.Pix.from_iter(((1, 0, 1, 0, 1, 0, 1, 0),
                         (0, 1, 0, 1, 0, 1, 0, 1),
                         (1, 0, 1, 0, 1, 0, 1, 0),
                         (0, 1, 0, 1, 0, 1, 0, 1),
                         (1, 0, 1, 0, 1, 0, 1, 0),
                         (0, 1, 0, 1, 0, 1, 0, 1),
                         (1, 0, 1, 0, 1, 0, 1, 0),
                         (0, 1, 0, 1, 0, 1, 0, 1),))

food = (random.randint(0, 7), random.randint(0, 7))
speed = 1


while True:
    # Draw the food
    screen.blit(background)
    screen.pixel(food[0], food[1], 1)
    
    # Draw the snake
    for index, element in enumerate(snake):
        if (index != 0):
            screen.pixel(element[0], element[1], 3)
        else:
            screen.pixel(element[0], element[1], 3 if blink == True else 2)
            blink = not blink

    # User Input
    keys = pew.keys()
    if (keys & pew.K_UP) and (dy != 1):
        dx = 0
        dy = -1
    elif (keys & pew.K_DOWN) and (dy != -1):
        dx = 0
        dy = 1
    elif (keys & pew.K_LEFT) and (dx != 1):
        dx = -1
        dy = 0
    elif (keys & pew.K_RIGHT) and (dx != 1):
        dx = 1
        dy = 0

    # Check if the snake is eating
    head = snake[0]
    if head != food:
        snake.pop()
    else:
        food = (random.randint(0, 7), random.randint(0, 7)) 
        speed = speed * 1.1

    snake.insert(0, ((head[0] + dx) % 8, (head[1] + dy) % 8))
    head = snake[0]
    if head in snake[1:]:
        break

    pew.show(screen)
    pew.tick(1/speed)

while True:
    screen.blit(end)
    pew.show(screen)
    pew.tick(1)