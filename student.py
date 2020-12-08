from datetime import datetime
from dateutil.relativedelta import relativedelta


class Student():
  # This is where the chunch of the workis happening, a student is a component of Floor 
    def __init__(self, id, name, email, DoB, unit, hobbies, status=None, events=None, followers=None):
        self.__id = id
        self.name = name
        self.__email = email
        self.__DoB = DoB #date of birth
        self.__unit = unit #the dorm unit of student
        self.hobbies = hobbies
        self.status = status or "Down to Chill" #the status the student wants to show to others
        self.events = events or [] #the events the student will attend
        self.followers = followers or [] #Students can follow other students (if they change status or attend an event)

    def get_id(self):
        return self.id
    
    def get_events(self):
      return self.events

    def get_age(self):
      # this calculates the age of the person without forgoing sensitive information like the date of birth when shown on the console
        start_date = datetime.now()
        end_date = self.__DoB
        difference_in_years = relativedelta(start_date, end_date).years
        return difference_in_years

    def get_status(self):
      #get the current status of the student
        return self.status

    def set_status(self, status):
      # this is the only set function in all the code. this sets the status and notfiies the users about it (by printing it on the console for now)
        self.status = status
        self.notify_followers("set", status, "status")

    def add_event(self, event):
      # adds an event to the events list and notifies followert
        self.events.append(event)
        self.notify_followers("added", event, "event")

    def add_follower(self,  student):
      #adds a student follower to the list and notifies followers
        self.followers.append(student)
        self.notify_followers("following", student)

    def notify_followers(self, verb, value_changed, key_changed=None):
      # this method is meant to handle the different cases of communication to print for followers
        if verb == 'set':
            print()
            print(
                f"{self.name} has {verb} their {key_changed} to {value_changed.name}")
        elif verb == 'following':
            print()
            print(
                f"{self.name} has started {verb} {value_changed.name}")
        else:
            print()
            print(
                f"{self.name} has {verb} an {key_changed} named {value_changed.name}")

    def remove_event(self, event):
      # remove the event, if not found print an error message
        try:
            self.events.remove(event)
        except ValueError:
            print(f"{event.name} does not exist in {self.name}")

    def __repr__(self):
      # A nice sttring representation of the instance for the developer
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
      """
