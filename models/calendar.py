from models.event import *
# import datetime

# event1 = Event(datetime.date(2021, 11, 10), "Gala Dinner", 100, "Main Hall", "Gala dinner for Edinburgh Chamber of Commerce", False)
# event2= Event(datetime.date(2021, 11, 30), "Ceilidh", 30, "Ballroom", "Monthly ceilidh", True)

event1 = Event("2021", "Gala Dinner", 100, "Main Hall", "Gala dinner for Edinburgh Chamber of Commerce", False)
event2= Event("2022", "Ceilidh", 30, "Ballroom", "Monthly ceilidh", True)

events = [event1, event2]

def add_new_event(new_event):
    events.append(new_event)