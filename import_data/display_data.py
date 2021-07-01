import pyglet
import time

window = pyglet.window.Window(1600, 1100)
image = pyglet.resource.image('media/supermarket.jpeg')

# music = pyglet.resource.media('media/music.mp3')
# music.play()

# entrance, pink
# fruit, green
# dairy, orangey yellow
# spices, red
# drinks, blue
# checkout, black
# end - yellow

ball_image = pyglet.image.load('import_data/media/sprite.jpg')
ball = pyglet.sprite.Sprite(ball_image, x=600, y=150)


@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)
    ball.draw()


pyglet.app.run()
