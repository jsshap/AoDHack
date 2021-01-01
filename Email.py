import time
import datetime as dt

class Email:

    '''
    Event has:
    list:names
    list:emails
    ????:time
    String:location
    '''

    def notify(event):
        participants=event.participants
        emails=event.emails
        location=event.location

