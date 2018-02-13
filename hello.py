import random
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

moves = ['rock', 'paper', 'scissors']
images = {move: pyglet.resource.image('%s.png' % move) for move in moves}

for image in images.itervalues():
    image.anchor_y = image.width//2
    image.anchor_x = image.height//2

computer_move = None
player_move = None

to_blit = []


def update_countdown(dt, text):
    countdown.text = text


def run_round(dt):
    global player_move
    global computer_move
    player_move = user_selection.text or random.choice(moves)
    computer_move = random.choice(moves)
    update_countdown(None, 'Go!')


def score(player_move, computer_move):
    if player_move == computer_move:
        return 'Tie'


def show_results(dt):
    to_blit.append((images[computer_move], window.width//2, window.height * .75))
    to_blit.append((images[player_move], window.width//2, window.height * .30))
    update_countdown(None, score(player_move, computer_move))


pyglet.clock.schedule_once(update_countdown, 1, text='3')
pyglet.clock.schedule_once(update_countdown, 2, text='2')
pyglet.clock.schedule_once(update_countdown, 3, text='1')
pyglet.clock.schedule_once(run_round, 4)
pyglet.clock.schedule_once(show_results, 4.5)


@window.event
def on_draw():
    window.clear()
    for image, x, y in to_blit:
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
    user_selection.text = key_actions.get(symbol, user_selection.text)


if __name__ == '__main__':
    pyglet.app.run()
