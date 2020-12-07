class Institution():
    def __init__(self, name, residences=[]):
        self.name = name
        self.residences = residences
    
    def add_residences(self, residence):
          self.residence.append(residence)
    
    def remove_residence(self, residence):
      try:
        self.residences.remove(residence)
      except ValueError:
        print(f"{residence.name} does not exist in {self.name}")

