from voxel import Voxel


def generate_terrain(width, depth, grass_texture, block_manager, punch_sound):
    for z in range(depth):
        for x in range(width):
            Voxel(
                position=(x, 0, z),
                texture=grass_texture,
                block_manager=block_manager,
                punch_sound=punch_sound,
            )