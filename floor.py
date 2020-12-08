class Floor():
    def __init__(self, name, students=None):
        self.name = name
        self.students = students or []
    
    def get_students(self):
      return self.students

    def add_student(self, student):
        self.students.append(student)
        # print(self.name)
        # print(self.students)

    def remove_student(self, student):
        try:
            self.students.remove(student)
        except ValueError:
            print(f"{student.name} does not exist in {self.name}")
    
    def __repr__(self):
      student_names = []

      for student in self.students:
        student_names.append(student.name)

      return f"""
      Floor: {self.name}
      Students: {student_names}
      """
