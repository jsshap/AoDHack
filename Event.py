
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

    def __init__(self, min: int, max: int, location: str, time: str, title: str, description: str):
        self.participants=[]
        #self.participants.append(Participant(emailOfCreator,nameOfCreator))
        #test
        self.location= location
        self.time=time
        self.title=title
        self.numPeople = 1

        self.min=min

        #later implement no limit
        self.max = max

        self.description= description


    #TODO idk why the for loop doesn't work but the other one does
    def addParticipants(self, personList):
        for person in personList:
            self.participants.append[person]

        self.participants.append(personList[0])


    def getParticpants(self):
        return self.participants
    
    def getTime(self):
        return self.time
    
    