from Student import Student


class EventOrganiser(Student):
    def __init__(self, id, name, email, DoB, unit, hobbies, event, status=None, events=None, followers=None):
        super().__init__(id, name, email, DoB, unit, hobbies, status, events, followers)
        self.event = event
        self.events.append(event)

    def add_student_to_event(self, student):
        self.event._add_student(student)

    def remove_student_from_event(self, student):
      self.event._remove_student(student)
    
    def __repr__(self):
      event_names = []
      follower_names = []

      for event in self.events:
        event_names.append(event.name)

      for student in self.followers:
        follower_names.append(student.name)

      return f"""
      Student: {self.name}
      Age: {self.get_age()}
      Unit: {self._unit}
      Hobbies: {self.hobbies}
      Events Attending: {event_names}
      Followers: {follower_names}
      Organises: {self.event.name}
      """
