import pew
pew.init()
screen = pew.Pix()

x, y = 3, 0
dx, dy = 1, 1

while True:
    screen.pixel(x,y,0)

    

    if x + dx > 7 or x + dx < 0:
        dx = -dx
    if y + dy > 7 or y + dy < 0:
        dy = -dy
        
    x += dx
    y += dy

    screen.pixel(x,y,3)
    pew.show(screen)
    pew.tick(1/12)
