import random
from ability import Ability

class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use integer division to find half of the max_damage value
        # then return a random integer between half of max_damage and max_damage
        random_number = random.randint((int(self.max_damage) // 2), int(self.max_damage))
        return random_number