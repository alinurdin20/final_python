class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    def double_speed(self):
        self.speed *= 2

    def double_damage(self):
        self.damage *= 2

    def double_health(self):
        self.health *= 2

warrior = Character(100, 50, 10)
ninja = Character(80, 40, 40)

warrior.double_speed()
ninja.double_speed()

warrior.double_damage()
ninja.double_damage()

warrior.double_health()  
ninja.double_health()

print(f"Warrior Speed: {warrior.speed}")
print(f"Ninja Speed: {ninja.speed}")
print(f"Warrior Damage: {warrior.damage}")
print(f"Ninja Damage: {ninja.damage}")
print(f"Warrior Health: {warrior.health}")
print(f"Ninja Health: {ninja.health}")
