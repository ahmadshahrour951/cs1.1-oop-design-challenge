class Event():
  # Event is the final component. It is a component of Student.
    def __init__(self, name, description, address, start_time, end_time, img_url, students=None):
        self.name = name
        self.description = description
        self.address = address
        self.start_time = start_time #event start_time
        self.end_time = end_time #event end_time
        self.img_url = img_url #an online public URL
        self.students = students or [] #an event can have many studentds
    
    def get_students(self):
      # get the most important attribute
      return self.students

    def _add_student(self, student):
      #here student.add_event(self) refers to the current instance, hence it works
        self.students.append(student)
        student.add_event(self)

    def _remove_student(self, student):
      # remove the student from the event. Otherwise print an error message
        try:
            self.students.remove(student)
            student.remove_event(self)
        except ValueError:
            print(f"{student.name} does not exist in {self.name}")
    
    def __repr__(self):
      student_names = []

      for student in self.students:
        student_names.append(student.name)

      return f"""
      Event: {self.name}
      Description: {self.description}
      Address: {self.address}
      Start Time: {self.start_time}
      End Time: {self.end_time}
      Image Url: {self.img_url}
      Students: {student_names}
      """
