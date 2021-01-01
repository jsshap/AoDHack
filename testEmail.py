from send import sendEmail
import send
from Event import Event
from Participant import Participant

testEvent= Event(0, 100, "Pratt", '12:00', 'Title', 'Desc')
testEvent.participants.append(Participant('frisboysproject@gmail.com','Sung'))

send.sendEmail(testEvent)
