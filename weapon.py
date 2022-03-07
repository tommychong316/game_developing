class Weapon:
    def __init__(self, name, attack_power) -> None:
        self.name = name
        self.attack_power = attack_power
        
    def weapon_name(self):
        self.name = ""

    def weapon_power(self):
        self.attack_power = int
    
    def weapon_info(self):
        return '{} {}'.format(self.name, self.attack_power)

weapon1 = Weapon("Mace Power:", 30)
weapon2 = Weapon("Axe Power:", 30)
weapon3 = Weapon("Meteor Gun Power:", 100)









