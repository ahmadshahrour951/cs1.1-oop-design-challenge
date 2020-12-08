class Residence():
    # A residence is most probably a building, hence it would have floors. Residence is a component of Institution Class
    def __init__(self, name, address, floors=None):
        self.name = name
        self.address = address
        # A residence can have many floors
        self.floors = floors or []

    def get_floors(self):
      # A get method to retrieve the most important data
      return self.floors

    def add_floor(self,  floor):
      # One can add a floor to the residence
        self.floors.append(floor)

    def remove_floor(self, floor):
      # One can also remove a floor. This will through an error if the floor is not found
        try:
            self.floors.remove(floor)
        except ValueError:
            print(f"{floor.name} does not exist in {self.name}")
    
    def __repr__(self):
      # A nice way to represent the data with the most important information
      floor_names = []

      for floor in self.floors:
        floor_names.append(floor.name)

      return f"""
      Residence: {self.name}
      Address: {self.address}
      Floors: {floor_names}
      """
