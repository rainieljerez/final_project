from ursina import Ursina, window, held_keys
from ursina.prefabs.first_person_controller import FirstPersonController

from game_assets import load_textures, load_punch_sound
from block_manager import BlockManager
from sky import Sky
from hand import Hand
from world import generate_terrain
from hud import Hud

app = Ursina()

textures = load_textures()
punch_sound = load_punch_sound()
block_manager = BlockManager(textures)

window.fps_counter.enabled = False
window.exit_button.visible = True

generate_terrain(
    width=20,
    depth=20,
    grass_texture=textures["grass"],
    block_manager=block_manager,
    punch_sound=punch_sound,
)

player = FirstPersonController()
sky = Sky(textures["sky"])
hand = Hand(textures["arm"])
hud = Hud(block_manager)


def update():
    if held_keys["left mouse"] or held_keys["right mouse"]:
        hand.active()
    else:
        hand.passive()

    for key in ("1", "2", "3", "4"):
        if held_keys[key]:
            block_manager.select(key)
            hud.refresh()


app.run()