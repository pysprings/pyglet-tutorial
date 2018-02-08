import pyglet

window = pyglet.window.Window()
label = pyglet.text.Label('Hello, World!')


@window.event
def on_draw():
    window.clear()
    label.draw()


if __name__ == '__main__':
    pyglet.app.run()
