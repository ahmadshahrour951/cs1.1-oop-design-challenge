from datetime import datetime

# Get all the classes
from Institution import Institution
from Residence import Residence
from Floor import Floor
from Student import Student
from Event import Event
from EventOrganiser import EventOrganiser

# Define the Variables
institution = Institution("Make School")
residence = Residence(
    "The Herbert Hotel",
    "161 Powell St, San Francisco, CA 94102, United States"
)

floor_1 = Floor("Floor 1")
floor_2 = Floor("Floor 2")

student_1 = Student('1', 'Ahmed Shahrour', 'ahmed.shahrour@students.makeschool.com',
                    datetime(1985, 9, 17), '112', ['Hiking', 'IoT', 'Star Gazing', 'Philosophy'], "Down to Chill")

event = Event('Road Trip to Yosemite National Park', 'This trip will blow your mind! The stars and galaxies are just waiting for you to see them! There are bears so make sure you spray around your territory with a bear deterrent.',
              'Yosemite National Park, Yosemite Valley, CA 95389, United States', datetime(2021, 3, 1), datetime(2021, 3, 3), 'https://images.newindianexpress.com/uploads/user/imagelibrary/2020/6/4/w900X450/Walk_in_the_Woods.jpg')
student_2 = EventOrganiser('2', 'Richard Jacobson', 'richard.jacobson@students.makeschool.com',
                           datetime(1995, 12, 2), '217', ['Philosophy', 'Psychology', 'IoT'], event, "Occupied")

student_3 = Student('3', 'Nolan Ngo', 'nolan.ngo@students.makeschool.com',
                    datetime(1985, 9, 17), '211', ['Hiking', 'IoT', 'Star Gazing', 'Philosophy'], "Down to Chill")

# Lets relate these variables and make them functional
institution.add_residence(residence)

residence.add_floor(floor_1)
residence.add_floor(floor_2)

floor_1.add_student(student_1)

floor_2.add_student(student_2)
floor_2.add_student(student_3)

student_2.add_student_to_event(student_1)
student_2.add_student_to_event(student_3)

student_3.add_follower(student_1)

# Lets see the insides of each of the instances, expectation vs reality (i.e. testing)
# print(institution)
# print(residence)
# print(floor_1)
# print(floor_2)
# print(event)
# print(student_1)
# print(student_2)
# print(student_3)
