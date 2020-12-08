from datetime import datetime
from dateutil.relativedelta import relativedelta


class Student():
    def __init__(self, id, name, email, DoB, unit, hobbies, status=None, events=None, followers=None):
        self.__id = id
        self.name = name
        self.__email = email
        self.__DoB = DoB
        self.__unit = unit
        self.hobbies = hobbies
        self.status = status or "Down to Chill"
        self.events = events or []
        self.followers = followers or []

    def get_id(self):
        return self.id
    
    def get_events(self):
      return self.events

    def get_age(self):
        start_date = datetime.now()
        end_date = self.__DoB
        difference_in_years = relativedelta(start_date, end_date).years
        return difference_in_years

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status
        self.notify_followers("set", status, "status")

    def add_event(self, event):
        self.events.append(event)
        self.notify_followers("added", event, "event")

    def add_follower(self,  student):
        self.followers.append(student)
        self.notify_followers("following", student)

    def notify_followers(self, verb, value_changed, key_changed=None):
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
        try:
            self.events.remove(event)
        except ValueError:
            print(f"{event.name} does not exist in {self.name}")

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
      """
