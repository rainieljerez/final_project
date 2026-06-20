from abc import ABC, abstractmethod

class Block(ABC):
    @abstractmethod
    def get_texture(self):
        """Every concrete block type must say which texture it uses."""
        pass

    @abstractmethod
    def get_name(self):
        """Every concrete block type must say what it's called (for UI display)."""
        pass


class GrassBlock(Block):
    def __init__(self, texture):
        self._texture = texture  # ENCAPSULATION

    def get_texture(self):
        return self._texture

    def get_name(self):
        return "Grass"


class StoneBlock(Block):
    def __init__(self, texture):
        self._texture = texture

    def get_texture(self):
        return self._texture

    def get_name(self):
        return "Stone"


class BrickBlock(Block):
    def __init__(self, texture):
        self._texture = texture

    def get_texture(self):
        return self._texture

    def get_name(self):
        return "Brick"


class DirtBlock(Block):
    def __init__(self, texture):
        self._texture = texture

    def get_texture(self):
        return self._texture

    def get_name(self):
        return "Dirt"