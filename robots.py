from weapon import Weapon

weapon1 = Weapon("Mace", 45)
weapon2 = Weapon("Axe", 40)
weapon3 = Weapon("Meteor Gunn", 100)

class Robot:
    def __init__(self, name, health, equipped_weapon) -> None:
        self.name = name
        self.health = health 
        self.equipped_weapon = equipped_weapon
        self.weapons = []
        print(name, health, equipped_weapon)

    def robot_name(self):
        self.name = ""

    def robot_health(self):
        self.health = int
        
    def equip_weapon(self, weapon):

        if len(self.weapons) <= self.equipped_weapon:
            self.equip_weapon = EW
            self.weapons.append(weapon)
            return True
        return False
    
EW = "Equipped Weapon: "
WP = "Weapon Power: "

robot1 = Robot("Jarvis", 125, 1)
robot1.equip_weapon(weapon1)
print(EW, robot1.weapons[0].name)
print(WP, robot1.weapons[0].attack_power)

robot2 = Robot("Small Wonder", 125, 1)
robot2.equip_weapon(weapon2)
print(EW, robot2.weapons[0].name)
print(WP, robot2.weapons[0].attack_power)

robot3 = Robot("J5", 125, 1)
robot3.equip_weapon(weapon3)
print(EW, robot3.weapons[0].name)
print(WP, robot3.weapons[0].attack_power)

