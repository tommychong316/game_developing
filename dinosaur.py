

class Dinosaur:
    def __init__(self, name, health, attack_power) -> None:
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def dino_name(self):
        self.name = ""
    def dino_health(self):
        self.health = int
    def dino_attack_power(self):
        self.attack_power = int
    
dino1 = Dinosaur("Not da Mama", 300, 25)
dino2 = Dinosaur("Ducky", 300, 25)
dino3 = Dinosaur("Yoshi", 300, 25)
    