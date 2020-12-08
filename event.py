class Event():
    def __init__(self, name, description, address, start_time, end_time, img_url, students=None):
        self.name = name
        self.description = description
        self.address = address
        self.start_time = start_time
        self.end_time = end_time
        self.img_url = img_url
        self.students = students or []
    
    def get_students(self):
      return self.students

    def _add_student(self, student):
        self.students.append(student)
        student.add_event(self)

    def _remove_student(self, student):
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
