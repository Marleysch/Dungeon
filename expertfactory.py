import enemyfactory
import zombie
import skeleton
import goblin
import random

class Expert_Factory(enemyfactory.Enemy_Factory):
  def create_random_enemy(self):
    random_enemy = random.choice(['zombie', 'skeleton', 'goblin'])
    if random_enemy == 'zombie':
      return zombie.Zombie("Fast Zombie",random.randint(8,10))
    elif random_enemy == 'skeleton':
      return skeleton.Skeleton("Archer Skeleton",random.randint(6,10))
    elif random_enemy == 'goblin':
      return goblin.Goblin("Angry Goblin",random.randint(8,12))