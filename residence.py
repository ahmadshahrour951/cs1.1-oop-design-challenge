class Residence():
    def __init__(self, name, address, floors=[]):
        self.name = name
        self.address = address
        self.floors = floors

    def add_floors(self,  floors):
      for floor in floors:
          self.floors.append(floor)

    def remove_floor(self, floor):
      try:
        self.floors.remove(floor)
      except ValueError:
        print(f"{floor.name} does not exist in {self.name}")
