import entity
import random

class Skeleton(entity.Entity):
  def __init__(self, name, max_hp):
    super().__init__(name, max_hp)
    # self.name = "Archer Skeleton"
    # self.max_hp = random.randint(6,10)
    self.hp = self.max_hp

  def attack(self, entity):
    dmg = random.randint(6,10)
    entity.take_damage(dmg)
    print(self.name + " attacks " + entity.name + " for " + str(dmg) + " damage.")