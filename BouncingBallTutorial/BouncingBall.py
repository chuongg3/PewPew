import pew

pew.init()
screen = pew.Pix()

x, y = 3, 0
dx, dy = 1, 1

ball = pew.Pix.from_iter(((3, 2),
                          (2, 1)))

background = pew.Pix.from_iter(((1, 0, 1, 0, 1, 0, 1, 0),
                                (0, 1, 0, 1, 0, 1, 0, 1),
                                (1, 0, 1, 0, 1, 0, 1, 0),
                                (0, 1, 0, 1, 0, 1, 0, 1),
                                (1, 0, 1, 0, 1, 0, 1, 0),
                                (0, 1, 0, 1, 0, 1, 0, 1),
                                (1, 0, 1, 0, 1, 0, 1, 0),
                                (0, 1, 0, 1, 0, 1, 0, 1),))

while True:
    keys = pew.keys()
    screen.blit(background)

    if x + dx > 6 or x + dx < 0 or keys & pew.K_O:
        dx = -dx
    if y + dy > 6 or y + dy < 0 or keys & pew.K_X:
        dy = -dy

    x += dx
    y += dy

    screen.blit(ball, x, y)

    pew.show(screen)
    pew.tick(1/5)
