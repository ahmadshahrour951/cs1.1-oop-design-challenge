class Residence():
    def __init__(self, name, address, floors=None):
        self.name = name
        self.address = address
        self.floors = floors or []

    def get_floors(self):
      return self.floors

    def add_floor(self,  floor):
        self.floors.append(floor)

    def remove_floor(self, floor):
        try:
            self.floors.remove(floor)
        except ValueError:
            print(f"{floor.name} does not exist in {self.name}")
    
    def __repr__(self):
      floor_names = []

      for floor in self.floors:
        floor_names.append(floor.name)

      return f"""
      Residence: {self.name}
      Address: {self.address}
      Floors: {floor_names}
      """
