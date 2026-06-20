from ursina import load_texture, Audio


def load_textures():
    return {
        "grass": load_texture("assets/grass_block.png"),
        "stone": load_texture("assets/stone_block.png"),
        "brick": load_texture("assets/brick_block.png"),
        "dirt": load_texture("assets/dirt_block.png"),
        "sky": load_texture("assets/skybox.png"),
        "arm": load_texture("assets/arm_texture.png"),
    }


def load_punch_sound():
    return Audio("assets/punch_sound", loop=False, autoplay=False)