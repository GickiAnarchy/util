#
#

class BodyPart:
  part_name = "None"
  slots = 0
  availability = True

class Hands(BodyPart):
  def __init__(self):
    self.self = 2
    self.part_name = "Hands"