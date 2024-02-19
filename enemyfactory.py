import abc

class Enemy_Factory(abc.ABC):
  @abc.abstractmethod
  def create_random_enemy(self):
    pass

