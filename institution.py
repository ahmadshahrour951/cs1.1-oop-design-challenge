class Institution():
    # Institution will be the head of the UML. Everythin branches out from here.
    def __init__(self, name, residences=None):
        self.name = name
        # An institution can have many residences
        self.residences = residences or []
    
    def get_residences(self):
      # a simple get method for the main information which is the residences
      return self.residences

    def add_residence(self, residence):
      #The institution may have a new residence to add
      self.residences.append(residence)

    def remove_residence(self, residence):
      # Here the residence can be removed if it is found within the list attribute, otherwise print an error message
      try:
        self.residences.remove(residence)
      except ValueError:
        print(f"{residence.name} does not exist in {self.name}")
    
    def __repr__(self):
        # This is just a nice way to represent the data to the developer using the code
        residence_names = []
        for residence in self.residences:
          residence_names.append(residence.name)
        return f"""
        Institution: {self.name}
        Residences: {residence_names}
        """

