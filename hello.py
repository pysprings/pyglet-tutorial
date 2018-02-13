import pyglet

window = pyglet.window.Window()
label = pyglet.text.Label(
            'Hello, World!',
            font_name='Times New Roman',
            font_size=36,
            x=window.width//2, y=window.height//2,
            anchor_x='center', anchor_y='center'
        )
image = pyglet.resource.image('rock.png')


@window.event
def on_draw():
    window.clear()
    image.blit(window.width//2, window.height * .60)
    label.draw()


@window.event
def on_key_press(symbol, modifiers):
    label.text = pyglet.window.key.symbol_string(symbol)


if __name__ == '__main__':
    pyglet.app.run()
