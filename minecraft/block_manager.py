from blocks import GrassBlock, StoneBlock, BrickBlock, DirtBlock

class BlockManager:
    def __init__(self, textures):
        self._blocks = {
            "1": GrassBlock(textures["grass"]),
            "2": StoneBlock(textures["stone"]),
            "3": BrickBlock(textures["brick"]),
            "4": DirtBlock(textures["dirt"]),
        }
        self._selected_key = "1"

    def select(self, key):
        if key in self._blocks:
            self._selected_key = key

    def current_block(self):
        return self._blocks[self._selected_key]