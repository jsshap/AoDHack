
import time
import datetime as dt

import smtplib
from email.message import EmailMessage

class Email:

    '''
    Event has:
    list:names
    list:emails
    ????:time
    String:location

    String:type:sports/meal/something

    '''

    def notify(event):
        '''
        participants=event.participants
        emails=event.emails
        location=event.location
        '''


        #with open("email.txt") as fp:
        msg=EmailMessage()
        msg.set_content("Tets")

        msg['Subject']="Subject"
        msg['From']='frisboysproject@gmail.com'
        msg['To']='frisboysproject@gmail.com'

        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()


Email.notify(3)
