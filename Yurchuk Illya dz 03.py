import random

class Machine:
    def __init__(self, name="V1",specification = None , Creator = None, ability_to_fight = 0, weapons = 1, gun = None):
        self.name = name
        self.points = 862355
        self.defense = 0
        self.blood = 100

        def regenerate_health(self):
            pass
        def kill_enemy(self):
            pass
        def make_style(self):
            pass
        def get_gun(self):
            self.gun = guns(list_of_guns)

list_of_guns = {
    "Alternate revolver": {"damage": 2.5, "alt_fire_damage": 7.5, "fire_cd": 1.31, "alt_fire_cooldown": 5},
    "Core eject shootgun": {"damage": 3, "alt_fire_damage": 3.5, "fire_cd": 1.25, "alt_fire_cooldown": 2.3},
    "Sawblade launcher": {"damage": 0.75, "alt_fire_damage": 0, "fire_cd": 4.3, "alt_fire_cooldown": 0},
    "Electric Railcannon": {"damage": 8, "alf_fire_damage": 0, "fire_cd": 16, "alt_fire_cooldown": 0},
    "Rocket launcher": {"damage": 3.5, "alt_fire_damage": 0, 'fire_cd': 1, "alt_fire_cooldown": 10}
}
        
class guns:
    def __init__(self, gun_list):
        self.gun_list = random.choice(list(list_of_guns))
        self.damage = gun_list[self]["damage"]
        self.alt_fire_damage = gun_list[self]["alt_fire_damage"]
        self.fire_cd = gun_list[self]["fire_cd"]
        self.alt_fire_cooldown = gun_list[self]["alt_fire_cooldown"]

