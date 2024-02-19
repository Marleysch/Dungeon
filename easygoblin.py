import entity
import random

class Easy_Goblin(entity.Entity):
  def __init__(self, name, max_hp):
    super().__init__(name, max_hp)
    #self.name = "Timid Goblin"
    #self.max_hp = random.randint(4,6)
    self.hp = self.max_hp

  def attack(self, entity):
    dmg = random.randint(2,5)
    entity.take_damage(dmg)
    print(self.name + " attacks " + entity.name + " for " + str(dmg) + " damage.")