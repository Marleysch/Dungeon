import entity
import random
import map

# Creates a class for the hero
class Hero(entity.Entity):
  def __init__(self,name,max_hp):
    super().__init__(name,max_hp)
    self._loc = [0,0] #x, y
    self._map = map.Map()
    self._map.reveal(self._loc)

  def attack(self,entity):
    dmg = random.randint(2,5)
    entity.take_damage(dmg)
    print(self.name + " attacks " + entity.name + " for " + str(dmg) + " damage.")

  def go_north(self):
    if self._loc[1] == 0:
      # print("You can't go north.")
      return 'o'
    else:
      self._loc[1] -= 1
      self._map.reveal(self._loc)
      return self._map.show_map(self._loc)


  def go_south(self):
    if self._loc[1] + 1 >= len(self._map):
      # print("You can't go south.")
      return 'o'
    else:
      self._loc[1] += 1
      self._map.reveal(self._loc)
      return self._map.show_map(self._loc)

  def go_east(self):
    if self._loc[0] + 1 >= len(self._map[self._loc[0]]):
      # print("You can't go east.")
      return 'o'
    else:
      self._loc[0] += 1
      self._map.reveal(self._loc)
      return self._map.show_map(self._loc)

  def go_west(self):
    if self._loc[0] == 0:
      # print("You can't go west.")
      return 'o'
    else:
      self._loc[0] -= 1
      self._map.reveal(self._loc)
      return self._map.show_map(self._loc)