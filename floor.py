class Floor():
    # This is a component of the Residence and Institution classes
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def add_students(self, students):
      for student in students:
        self.students.append(student)
    
    def remove_student(self, student):
      try:
        self.students.remove(student)
      except ValueError:
        print(f"{student.name} does not exist in {self.name}")

