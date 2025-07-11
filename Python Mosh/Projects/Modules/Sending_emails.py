# helps you define the various parts of the email
from email.mime.multipart import MIMEMultipart
# helps you write text in the body of the email
from email.mime.text import MIMEText
# helps you write text in the body of the email
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib


template = Template(Path('template.html').read_text())


# mime : multipurpose internet mail extensions a standard for defining form of email messages

# creates an email object that would be sent
message = MIMEMultipart()
message['From'] = 'Mosh Hamedani'
message['to'] = 'testuser@gmail.com'
message['subject'] = 'this is a test'
body = template.substitute({'name': 'John'})
message.attach(MIMEText(body, 'html'))
# sends pic in the given directory as a byte data
message.attach(MIMEImage(Path('mosh.png').read_bytes()))

# now to send it
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # message sent to the smtp server
    smtp.starttls()
    smtp.login('testuser@gmail.com', 'Acity2023.')
    smtp.send_message(message)
    print('sent...')
