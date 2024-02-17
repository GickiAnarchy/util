#
#
from human import *

class Game:
  def __init__(self):
    self.player = Human()
    #self.player2 = Human()
    self.player.create()
    #self.player2.create()
    g = PosEvent()


if __name__ == "__main__":
  game = Game()
  