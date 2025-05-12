class Enemy:
    def __init__(self, health, distance, speed, x, y):
        self.health = health
        self.distance = distance
        self.speed = speed
        self.x = x
        self.y = y
    @classmethod
    def create(cls, health, speed, x, y):
        distance = 0
        return cls(health, distance, speed, x, y)

enemy1: Enemy = Enemy.create(15, 1, 0, 0)
