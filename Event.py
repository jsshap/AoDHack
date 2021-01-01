
'''
Fields:

list: Participant objects
?????: time
String: location
????: type of event 

methods:

getParticipants()--> return list

getTime() --> return time

getLocation() --> return string

getType() --> return

'''

from Participant import Participant


class Event:

    def __init__(self, emailOfCreator: str, nameOfCreator: str, min: int, max: int, location: str, time: str, description: str):
        self.participants=[]
        self.participants.append(Participant(emailOfCreator,nameOfCreator))

        self.location= location
        self.time=time

        self.numPeople = 1

        self.min=min

        #later implement no limit
        self.max = max

        self.description= description

    def getParticpants(self):
        return self.participants
    
    def getTime(self):
        return self.time
    
    