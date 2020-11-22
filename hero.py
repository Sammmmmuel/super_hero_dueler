import random 
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()

    def add_ability(self, ability):
        '''Add ability to abilities list '''
        # use append method to add ability to our list
        self.abilities.append(ability)

    def add_armor(self, armor):
        '''Add armor to armors list '''
        # use apppend method to add armor to our list
        self.armors.append(armor)
    
    # def fight(self, opponent):
    #     winner = random.choice([self.name, opponent.name])
    #     print(f'{winner} is the winner!')

    def attack(self):
        '''Calculate the total damage from all ability attacks.'''

    # start our total out at 0
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage

    def defend(self, damage_amt):
        ''' Calculate total block amount from all armor'''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return damage_amt - total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        # TODO: Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        self.current_health -= self.defend(damage)

    def is_alive(self):  
        '''Return True or False depending on whether the hero is alive or not.
        '''
        # TODO: Check the current_health of the hero.
        # if it is <= 0, then return False. Otherwise, they still have health
        # and are therefore alive, so return True
        if self.current_health <= 0:
            return False
        else: 
            return True

    def fight(self, opponent):  
# ''' Current Hero will take turns fighting the opponent hero passed in.'''
# TODO: Fight each hero until a victor emerges.
# Phases to implement:
# 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
# 1) else, start the fighting loop until a hero has won
# 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
# 3) After each attack, check if either the hero (self) or the opponent is alive
# 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw!")
            return
        else:
            while self.is_alive() == True and opponent.is_alive() == True:
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
            if self.is_alive() == True:
                print(f"{self.name} won")
            elif opponent.is_alive() == True:
                print(f"{opponent.name} won")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
