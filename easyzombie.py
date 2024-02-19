import entity
import random

class Easy_Zombie(entity.Entity):
  def __init__(self, name, max_hp):
    super().__init__(name, max_hp)
    # self.name = "Slow Zombie"
    # self.max_hp = random.randint(4,5)
    self.hp = self.max_hp

  def attack(self, entity):
    dmg = random.randint(1,5)
    entity.take_damage(dmg)
    print(self.name + " attacks " + entity.name + " for " + str(dmg) + " damage.")