from ursina import Entity, scene


class Sky(Entity):
    def __init__(self, texture):
        super().__init__(
            parent=scene,
            model="sphere",
            texture=texture,
            scale=150,
            double_sided=True,
        )