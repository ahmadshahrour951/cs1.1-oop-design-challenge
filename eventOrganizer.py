import Student

class EventOrganizer(Student):
  def __init__(self, event):
    super().__init__()
    self.event = event