import smtplib
import email
from email.mime.multipart import MIMEMultipart
#from email.MIMEText import MIMEText

'''
Event has:
list: Participants (each participant has name and email field)
????:time
String:location

String:type:sports/meal/something

Description (can be null): string

'''
sender_email = 'frisboysproject@gmail.com'
password = 'amherst123'


def sendEmail(event):    
    participants=event.participants
    

    receiver_emails = []
    for p in participants:
        receiver_emails.append(p.getEmail())


    names=[]
    for p in participants:
        names.append(p.getName())


    # Email text
    email_body = '''Subject: Your Hangout Event\n
    \nHello, you have an update from Hangout!
    '''

    email_body+=('\nYour event is on!\n\n' +"\nTime: "+event.time+ "\nTitle: " + event.title + "\nDescription: " + event.description+ "\nLocation: " + event.location +"\n\nParticipants:\n")

    for count, name in enumerate(names):
        email_body+=("\n"+str(count)+". "+  name)

    email_body += ("\n\n\nSee you there!")
    

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(sender_email, password)
    # Sending email from sender, to receiver with the email body
    server.sendmail(sender_email, receiver_emails, email_body)
    print('Email sent!')

    print('Closing the server...')
    server.quit()