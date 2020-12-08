from Student import Student


class EventOrganiser(Student):
  # This is a subclass of the Student class, the reason being is that not all students are allowed to alter the event. Only the event oraganiser can do that.
    def __init__(self, id, name, email, DoB, unit, hobbies, event, status=None, events=None, followers=None):
      # super() is used to inherit from the Student class. Then we add another attribute called event. Which is what the event organiser is organising
        super().__init__(id, name, email, DoB, unit, hobbies, status, events, followers)
        self.event = event
        self.events.append(event)

    def add_student_to_event(self, student):
      #this reference the method in the event object passed to add a student to the event for attendance
        self.event._add_student(student)

    def remove_student_from_event(self, student):
      # this is a method to remove student ftom the event. if not found print an error message
      try:
        self.event._remove_student(student)
      except ValueError:
        print(f"{student.name} does not exist in {self.name}")
      
    
    def __repr__(self):
      # a nice string representation of the instance for the developer
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
