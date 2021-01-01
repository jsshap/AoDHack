import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.

    # Create a text/plain message
msg = EmailMessage()
#msg.set_content(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Test'
msg['From'] = "info@down2hang.co"
msg['To'] = 'frisboysproject@gmail.com'

# Send the message via our own SMTP server.
server = smtplib.SMTP('smtp.porkbun.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

server.login('info@down2hang.co', 'Amh3rst123')
    # Sending email from sender, to receiver with the email body
server.sendmail('info@down2hang.co', 'frisboysproject@gmail.com', msg['Subject'])
print('Email sent!')

print('Closing the server...')
server.quit()