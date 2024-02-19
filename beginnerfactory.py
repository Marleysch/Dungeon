import enemyfactory
import easyzombie
import easyskeleton
import easygoblin
import random

class Beginner_Factory(enemyfactory.Enemy_Factory):
  def create_random_enemy(self):
    random_enemy = random.choice(['zombie', 'skeleton', 'goblin'])
    if random_enemy == 'zombie':
      return easyzombie.Easy_Zombie("Slow Zombie", random.randint(4,5))
    elif random_enemy == 'skeleton':
      return easyskeleton.Easy_Skeleton("Weak Skeleton", random.randint(3,4))
    elif random_enemy == 'goblin':
      return easygoblin.Easy_Goblin("Timid Goblin", random.randint(4,6))