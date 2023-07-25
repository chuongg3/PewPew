import pew

pew.init()
screen = pew.Pix()

x, y = 3, 0
dx, dy = 1, 1

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

    if x + dx > 7 or x + dx < 0 or keys & pew.K_O:
        dx = -dx
    if y + dy > 7 or y + dy < 0 or keys & pew.K_X:
        dy = -dy

    x += dx
    y += dy

    screen.pixel(x,y,3)

    pew.show(screen)
    pew.tick(1/5)
