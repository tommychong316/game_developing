from herd import Herd
from fleet import Fleet 
from robots import Robot
from dinosaur import Dinosaur
from weapon import Weapon
import random

# class Weapon:
#     def __init__(self, name, attack_power) -> None:
#         self.name = name
#         self.attack_power = attack_power
        
#     def weapon_name(self):
#         self.name = ""

#     def weapon_power(self):
#         self.attack_power = int

# weapon1 = Weapon("Mace", 100)
# weapon2 = Weapon("Axe", 80)
# weapon3 = Weapon("Meteor Gunn", 120)

# class Robot:
#     def __init__(self, name, health, equipped_weapon) -> None:
#         self.name = name
#         self.helath = health 
#         self.equipped_weapon = equipped_weapon
#         self.weapons = []
#         print(name, health, equipped_weapon)

#     def robot_name(self):
#         self.name = ""

#     def robot_health(self):
#         self.health = int
    
#     def robot_attack(self, attack):
#         if self.weapons == 1:
#             Weapon.weapon_power = attack

#     def equip_weapon(self, weapon):
#         if len(self.weapons) <= self.equipped_weapon:
#             self.weapons.append(weapon)
#             return True
#         return False

# class Dinosaur:
#     def __init__(self, name, health, attack_power) -> None:
#         self.name = name
#         self.health = health
#         self.attack_power = attack_power
#     def dino_name(self):
#         self.name = ""
#     def dino_health(self):
#         self.health = int
#     def dino_attack_power(self):
#         self.attack_power = int
    
# dino1 = Dinosaur("Not da Mama", 300, 25)
# dino2 = Dinosaur("Ducky", 300, 25)
# dino3 = Dinosaur("Yoshi", 300, 25)


# print("---------------------------------")        
# robot1 = Robot("Jarvis", 125, 1)
# robot1.equip_weapon(weapon1)
# print("Jarvis' Weapon: ", robot1.weapons[0].name)
# print("Jarvis' Weapon's Power: ", robot1.weapons[0].attack_power)
# print("---------------------------------")
# robot2 = Robot("Small Wonder", 125, 1)
# robot2.equip_weapon(weapon2)
# print("Small Wonder's Weapon: ", robot2.weapons[0].name)
# print("Small Wonder's Weapon's Power: ", robot2.weapons[0].attack_power)
# print("---------------------------------")
# robot3 = Robot("J5", 125, 1)
# robot3.equip_weapon(weapon3)
# print("J5's Weapon: ", robot3.weapons[0].name)
# print("J5's Weapon Power: ", robot3.weapons[0].attack_power)

# class Fleet:
#     def __init__(self) -> None:
#         self.robots = []
   
# class Herd:
#     def __init__(self) -> None:
#         self.dinosaurs = []

# fleet = [robot1, robot2, robot3]
# herd = [dino1, dino2, dino3]

class Battlefield:
    
    def battle(self):
        while Robot.robot_health > 0 and Dinosaur.dino_health > 0:
            print(f"{Robot.robot_name}\t\tHLTH{Robot.robot_health}")
            print(f"{Dinosaur.dino_name}\t\tHLTH{Dinosaur.dino_name}")

            print(f"{Robot.robot_name} attacked")

            Dinosaur.dino_health -= random.randrange(80, 120)
            

            print(f"{Robot.robot_name}\t\tHLTH{Robot.robot_health}")
            print(f"{Dinosaur.dino_name}\t\tHLTH{Dinosaur.dino_name}")
        
            if Dinosaur.dino_health <= 0:
                print(f"..." + Dinosaur.dino_name + "died")
                break
            
            print(f"{Dinosaur.dino_name} attacked")

            Robot.robot_health -= 25
    
            print(f"{Robot.robot_name}\t\tHLTH{Robot.robot_health}")
            print(f"{Dinosaur.dino_name}\t\tHLTH{Dinosaur.dino_name}")
    
            if Robot.robot_health <= 0:
                print(f"..." + Robot.robot_name + "died")
                break

