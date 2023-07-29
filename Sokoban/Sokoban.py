import pew

pew.init()

screen = pew.Pix.from_iter(((1, 1, 1, 1, 1, 1, 1, 1),
                                (1, 0, 0, 0, 0, 0, 0, 1),
                                (1, 0, 0, 0, 0, 0, 0, 1),
                                (1, 0, 0, 0, 0, 0, 0, 1),
                                (1, 0, 0, 3, 0, 2, 0, 1),
                                (1, 0, 0, 0, 0, 0, 0, 1),
                                (1, 0, 0, 0, 0, 0, 0, 1),
                                (1, 1, 1, 1, 1, 1, 1, 1),))

player_x, player_y = 4, 1
blink = True

while True:
    screen.pixel(player_x, player_y, 0)

    keys = pew.keys()
    dx, dy = 0, 0
    if keys & pew.K_UP:
        dy = -1
    elif keys & pew.K_DOWN:
        dy = 1
    elif keys & pew.K_LEFT:
        dx = -1
    elif keys & pew.K_RIGHT:
        dx = 1

    target = screen.pixel(player_x + dx, player_y + dy)
    behind = screen.pixel(player_x + dx + dx, player_y + dy + dy)
    if target in {0, 2}:
        player_x += dx
        player_y += dy
    elif ((target == 3) and (behind in {0, 2})):
        screen.pixel(player_x + dx + dx, player_y + dy + dy, 3)
        player_x += dx
        player_y += dy
    screen.pixel(player_x, player_y, 3 if blink == True else 2)
    blink = not blink
    pew.show(screen)

    pew.tick(1/2)