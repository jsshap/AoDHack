from send import sendEmail
import send
from Event import Event

testEvent= Event('frisboysproject@gmail.com', 'Jake', 0, 100, "Pratt", '12:00', 'Desc')

send.sendEmail(testEvent)
