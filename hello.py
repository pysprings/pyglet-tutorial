import pyglet

window = pyglet.window.Window()
countdown = pyglet.text.Label(
            '',
            font_name='Times New Roman',
            font_size=36,
            x=window.width//2, y=window.height//2,
            anchor_x='center', anchor_y='center'
        )
user_selection = pyglet.text.Label(
            '',
            font_name='Times New Roman',
            font_size=36,
            x=window.width//2, y=window.height * .1,
            anchor_x='center', anchor_y='center'
        )
image = pyglet.resource.image('rock.png')
image.anchor_x = image.width // 2
image.anchor_y = image.height // 2

images = []


def update_countdown(dt, text):
    countdown.text = text


def run_round(dt):
    update_countdown(None, 'Go!')


pyglet.clock.schedule_once(update_countdown, 1, text='3')
pyglet.clock.schedule_once(update_countdown, 2, text='2')
pyglet.clock.schedule_once(update_countdown, 3, text='1')
pyglet.clock.schedule_once(run_round, 4)
pyglet.clock.schedule_once(lambda dt: images.append((image, window.width//2, window.height * .75)), 4.5)


@window.event
def on_draw():
    window.clear()
    for image, x, y in images:
        image.blit(x, y)
    countdown.draw()
    user_selection.draw()


key_actions = {
    pyglet.window.key.R: 'rock',
    pyglet.window.key.P: 'paper',
    pyglet.window.key.S: 'scissors'
}


@window.event
def on_key_press(symbol, modifiers):
    user_selection.text = key_actions.get(symbol, '')


if __name__ == '__main__':
    pyglet.app.run()
