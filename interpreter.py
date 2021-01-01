#JSON interpreter which turns JSON file into an Event object
import json
from Event import Event
from Participant import Participant

x =  '{ "min":5, "max": 10, "Location":"Hills Field", "Time":"2:30", "Description":"Practice", "Title":"Prac", "Participants":[{"Name":"Jake", "Email":"jsshap@gmail.com"}]}'

def JSONtoEvent(j: json):
    event= Event(j["min"], j["max"], j["Location"], j["Time"], j["Title"], j["Description"])
    for participant in j["Participants"]:
        event.participants.append(Participant(participant["Name"], participant["Email"]))
    
    return event

'''
parse = json.loads(x)
print(JSONtoEvent(parse))

event=JSONtoEvent(parse)
'''







