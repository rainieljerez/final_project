from ursina import Button, color, scene, mouse, destroy
import random

class Voxel(Button):
    def __init__(self, position, texture, block_manager, punch_sound):
        super().__init__(
            parent=scene,
            position=position,
            model="assets/block",
            origin_y=0.5,
            texture=texture,
            color=color.hsv(0, 0, random.uniform(0.9, 1)),
            scale=0.5,
        )
        self._block_manager = block_manager
        self._punch_sound = punch_sound

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self._punch_sound.play()
                new_block = self._block_manager.current_block()
                Voxel(
                    position=self.position + mouse.normal,
                    texture=new_block.get_texture(),
                    block_manager=self._block_manager,
                    punch_sound=self._punch_sound,
                )
            if key == "right mouse down":
                self._punch_sound.play()
                destroy(self)