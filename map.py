class Map:
  _instance = None
  _initialized = False

  def __new__(cls, *args):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self):
    if not Map._initialized:
      self.map_list = []
      self.map_revealed_list = []
      

  def load_map(self, map_num):
    # Reading file and creating map list
    with open(f'map{map_num}.txt', 'r') as file:
      self.map_list = []
      map_lines = file.readlines()
      for line in map_lines:
        line = line.strip()
        self.map_list.append(list(line))
      file.close()

    #Creating revealed spaces list
    self.map_revealed_list = []
    for i in range(len(self.map_list)):
      self.map_revealed_list.append([])
      for j in range(len(self.map_list[i])):
        self.map_revealed_list[i].append(False)

    Map._initialized = True
        
  def __getitem__(self, row):
    return self.map_list[row]

  def __len__(self):
    return len(self.map_list)

  def show_map(self, loc):
    map_str = ''
    for i in range(len(self.map_list)):
      if i != 0:
        map_str += '\n'
      for j in range(len(self.map_list[i])):
        if i == loc[1] and j == loc[0]:
          map_str += '*'
        elif not self.map_revealed_list[i][j]:
          map_str += 'x'
        else:
          map_str += self.map_list[i][j]
    return map_str

  def reveal(self, loc):
    self.map_revealed_list[loc[1]][loc[0]] = True

  def remove_at_loc(self, loc):
    self.map_list[loc[1]][loc[0]] = 'n'
