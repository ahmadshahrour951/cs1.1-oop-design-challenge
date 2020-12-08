class Floor():
  # Within each floor, there are students. Floor is a component of Residence
    def __init__(self, name, students=None):
        self.name = name
        # A floor has many students
        self.students = students or []
    
    def get_students(self):
      #simple get to return the students list
      return self.students

    def add_student(self, student):
      # add a student to the student list attribute
        self.students.append(student)

    def remove_student(self, student):
      #remove the student from the list using .remove(), otherwise print an error messge if not found
        try:
            self.students.remove(student)
        except ValueError:
            print(f"{student.name} does not exist in {self.name}")
    
    def __repr__(self):
      # Nice representation for the developer
      student_names = []

      for student in self.students:
        student_names.append(student.name)

      return f"""
      Floor: {self.name}
      Students: {student_names}
      """
