import spacegame
import pyglet, random

window = pyglet.window.Window(spacegame.config.WINDOW_WIDTH, spacegame.config.WINDOW_HEIGHT)
batch = pyglet.graphics.Batch()
minimap_batch = pyglet.graphics.Batch()


def update(dt):
	player.update(dt, player)
	background.update((player.xom, player.yom))
	minimap.update(player)
	for meteor in meteors:
		if not(meteor.dead):
			meteor.update(dt, player)
			if meteor.on_screen:
				if player.collides_with(meteor):
					meteor.dead = True
					meteor.delete()

background = spacegame.background.BackGround(batch=None)
minimap = spacegame.minimap.MiniMap(batch=minimap_batch)
player = spacegame.player.Player(batch=batch)
player.xom = 1000
player.yom = 1200

meteors = []
for x in range(0, spacegame.config.METEORS):
	meteor = spacegame.asteroid.Asteroid(batch=batch)
	meteor.xom = random.randint(0, spacegame.config.MAP_X)
	meteor.yom = random.randint(0, spacegame.config.MAP_Y)
	meteors.append(meteor)

@window.event
def on_draw():
	window.clear()

	#pozadí
	background.draw()

	#většina objektů
	batch.draw()

	#minimapa
	minimap_batch.draw()

@window.event
def on_key_press(symbol, modifiers):
	player.pressed_keys.append(symbol)

@window.event
def on_key_release(symbol, modifiers):
	player.pressed_keys.remove(symbol)

pyglet.clock.schedule_interval(update, 1 / spacegame.config.FPS)
pyglet.app.run()
