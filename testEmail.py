from send import sendEmail
import send
from classes import Participant, Event

testEvent= Event(0, 100, "Pratt Field", '12:00', 'Tossing with the boiz', 'Wanna Toss?')
testEvent.participants.append(Participant('frisboysproject@gmail.com','Sung'))
#testEvent.participants.append(Participant('test@gmail.com','Jake'))

send.sendEmail(testEvent)
