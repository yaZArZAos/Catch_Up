from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Бесконечные догонялки')
background = transform.scale(
    image.load('background.png'),
    (700, 500)
)

game = True
sprite1 = transform.scale(
    image.load('sprite1.png'),
    (50, 50)
)
sprite2 = transform.scale(
    image.load('sprite2.png'),
    (50, 50)
)
x1 = 150
y1 = 400
x2 = 550
y2 = 400

clock = time.Clock()
FPS = 60

while game:
    window.blit(background, (0, 0))
    window.blit(sprite1,(x1, y1))
    window.blit(sprite2,(x2, y2))
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(60)
    display.update()

    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP] and y2>0:
        y2 -= 10
    if keys_pressed[K_LEFT] and x2>0:
        x2 -= 10
    if keys_pressed[K_RIGHT] and x2<650:
        x2 += 10
    if keys_pressed[K_DOWN] and y2<450:
        y2 += 10

    if keys_pressed[K_w] and y1>0:
        y1 -= 10
    if keys_pressed[K_a] and x1>0:
        x1 -= 10
    if keys_pressed[K_d] and x1<650:
        x1 += 10
    if keys_pressed[K_s] and y1<450:
        y1 += 10

