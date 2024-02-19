import abc

# Creates a base class for all entities
class Entity(abc.ABC):
  def __init__(self, name, max_hp):
    self.name = name
    self.hp = max_hp
    self.max_hp = max_hp

  def take_damage(self, dmg):
    self.hp -= dmg
    if self.hp < 0:
      self.hp = 0

  def heal(self):
    self.hp = self.max_hp

  def __str__(self):
    return "Name: " + self.name + "\n" + "HP: " + str(self.hp) + "/" + str(self.max_hp)

  @abc.abstractmethod
  def attack(self, entity):
    pass
