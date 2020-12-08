class Institution():
    def __init__(self, name, residences=None):
        self.name = name
        self.residences = residences or []
    
    def get_residences(self):
      return self.residences

    def add_residence(self, residence):
      self.residences.append(residence)

    def remove_residence(self, residence):
      try:
        self.residences.remove(residence)
      except ValueError:
        print(f"{residence.name} does not exist in {self.name}")
    
    def __repr__(self):
        residence_names = []
        for residence in self.residences:
          residence_names.append(residence.name)
        return f"""
        Institution: {self.name}
        Residences: {residence_names}
        """

