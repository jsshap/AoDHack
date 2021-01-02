#JSON interpreter which turns JSON file into an Event object
import json
from Event import Event
from Participant import Participant

import testEmail

#x =  '{ "min":5, "max": 10, "Location":"Hills Field", "Time":"2:30", "Description":"Practice", "Title":"Prac", "Participants":[{"Name":"Jake", "Email":"frisboysproject@gmail.com"},{"Name":"Jordy", "Email":"jordypg@gmail.com"}]}'

def JSONtoEvent(j: json):
    print (j)
    event= Event(j["min"], j["max"], j["Location"], j["Time"], j["Title"], j["Description"])

    persons=[]
    for participant in j["Participants"]:
        persons.append(Participant(participant[0]["Email"], participant[0]["Name"]))

    event.addParticipants(persons)
    
    return event

