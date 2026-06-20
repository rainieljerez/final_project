from ursina import Text, color


class Hud:
    def __init__(self, block_manager):
        self._block_manager = block_manager
        self._label = Text(
            text="",
            position=(0, -0.45),
            origin=(0, 0),
            scale=1.5,
            color=color.white,
            background=True,
        )
        self.refresh()

    def refresh(self):
        block_name = self._block_manager.current_block().get_name()
        self._label.text = f"Block: {block_name}  (Press 1-4 to switch)"