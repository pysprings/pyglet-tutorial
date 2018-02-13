import pyglet

window = pyglet.window.Window()
label = pyglet.text.Label(
            '',
            font_name='Times New Roman',
            font_size=36,
            x=window.width//2, y=window.height//2,
            anchor_x='center', anchor_y='center'
        )
image = pyglet.resource.image('rock.png')
image.anchor_x = image.width // 2
image.anchor_y = image.height // 2

images = []


def update_label(dt, text):
    label.text = text


pyglet.clock.schedule_once(update_label, 1, text='3')
pyglet.clock.schedule_once(update_label, 2, text='2')
pyglet.clock.schedule_once(update_label, 3, text='1')
pyglet.clock.schedule_once(update_label, 4, text='Go!')
pyglet.clock.schedule_once(lambda dt: images.append((image, window.width//2, window.height * .75)), 4.5)


@window.event
def on_draw():
    window.clear()
    for image, x, y in images:
        image.blit(x, y)
    label.draw()


@window.event
def on_key_press(symbol, modifiers):
    label.text = pyglet.window.key.symbol_string(symbol)


if __name__ == '__main__':
    pyglet.app.run()
