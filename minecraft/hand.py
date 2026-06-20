from ursina import Entity, camera, Vec3, Vec2


class Hand(Entity):
    def __init__(self, texture):
        super().__init__(
            parent=camera.ui,
            model="assets/arm",
            texture=texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6),
        )

    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)