

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

    def addParticipants(self, personList):
        for person in personList:
            self.participants.append(person)


    def getParticpants(self):
        return self.participants
    
    def getTime(self):
        return self.time

    def getLocation(self):
        return self.location

    def __str__(self):
        participantsString = ', '.join(str(people) for people in self.participants)

        return("Event title: " + self.title +
              "\nMin participants: " + str(self.min) +
              "\nMax participants: " + str(self.max) +
              "\nLocation: " + self.location +
              "\nDescription: " + self.description +
              "\nParticipants: " + participantsString)



#DEFINE PARTICIPANT
class Participant:

    def __init__(self, email, name):
        self.email=email
        self.name=name

    def getEmail(self):
        return self.email

    def getName(self):
        return self.name

    def __str__(self):
        return (self.name + " (" + self.email + ")")
