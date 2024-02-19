#Marley Schneider, Rene Trujillo
#11/06/23
# Program that has a user go through a dungeon crawler style game.
import map
import hero
import random
import check_input
import beginnerfactory
import expertfactory

# program that runs the game
def main():
  map_count = 1
  map1 = map.Map()
  map1.load_map(map_count)
  user_name = input("What is your name, traveler? ")
  # creates the hero
  hero1 = hero.Hero(user_name, 25)
  # Difficulty
  difficulty = check_input.get_int_range("Difficulty:\n1. Easy\n2. Expert",1, 2)
  # Enemy Factory
  if difficulty == 1:
    factory = beginnerfactory.Beginner_Factory()
  else:
    factory = expertfactory.Expert_Factory()
  while True:
    print(hero1)
    print(map1.show_map(hero1._loc))
    # gives player the option to choose direction
    print()
    print("1. Go North")
    print("2. Go South")
    print("3. Go East")
    print("4. Go West")
    print("5. Quit")
    user_choice = check_input.get_int_range("Enter Choice: ", 1,5)

    if user_choice == 1:
      curr_space = hero1.go_north()
    elif user_choice == 2:
      curr_space = hero1.go_south()
    elif user_choice == 3:
      curr_space = hero1.go_east()
    elif user_choice == 4:
      curr_space = hero1.go_west()
    else:
      print("User Quit")
      break

    if curr_space == 'o':
      print('You can\'t go that direction')
    else:
      curr_space = map1.map_list[hero1._loc[1]][hero1._loc[0]]

      #item space
      if curr_space == 'i':
        if hero1.hp == 25:
          print('You found a health potion, but you are full health. You leave it for later.')
        else:
          print('You found a health potion. You drink it to restore your health.')
          hero1.hp = 25
          map1.remove_at_loc(hero1._loc)

      #monster space
      elif curr_space == 'm':
        monster = factory.create_random_enemy()
        print(f'You encounter a {monster.name} \nHP: {monster.hp}/{monster.max_hp}')
        while True:
          print(f'1.Attack {monster.name}\n2.Run Away')
          choice = check_input.get_int_range('Enter choice: ', 1, 2)
          if choice == 1:
            hero1.attack(monster)
            if monster.hp <= 0:
              print(f'You killed the {monster.name}')
              map1.remove_at_loc(hero1._loc)
              break
            monster.attack(hero1)
          else:
            direction = 'o'
            while True:
              directions = random.choice([hero1.go_north, hero1.go_south, hero1.go_west, hero1.go_east])
              direction = directions()
              print(f'Direction: {direction}')
              if direction != 'o':
                break
            break
      elif curr_space == 'n':
        print('There is nothing here.')
      elif curr_space == 's':
        print('You wound up back at the start.')
      elif curr_space == 'f':
        map_count += 1
        if map_count == 4:
          map_count = 1
        print('Congratulations, you found the next cave')
        map1.load_map(map_count)
        for i in range(len(map1)):
          for j in range(len(map1[i])):
            if map1[i][j] == 's':
              hero1._loc = [j,i]
              map1.reveal(hero1._loc)
    print()

main()