import entity
import random

class Easy_Skeleton(entity.Entity):
  def __init__(self, name, max_hp):
    super().__init__(name, max_hp)
    #self.name = "Weak Skeleton"
    #self.max_hp = random.randint(3,4)
    self.hp = self.max_hp

  def attack(self, entity):
    dmg = random.randint(1,4)
    entity.take_damage(dmg)
    print(self.name + " attacks " + entity.name + " for " + str(dmg) + " damage.")