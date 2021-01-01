import smtplib

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
    location=event.location
    

    receiver_emails = []
    for p in participants:
        receiver_emails.append(p.getEmail())


    names=[]
    for p in participants:
        names.append(p.getName())


    # Email text
    email_body = '''Subject: Your Hangout Event\n
    Hello, you have an update from Hangout!


    
    '''

    for n in names:
        email_body+=(n+"\n")

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