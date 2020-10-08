import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

if __name__ == '__main__':
    html = Template(Path('index.html').read_text())
    email = EmailMessage()
    email['from'] = 'Nihar Kajla'
    email['to'] = 'niharamazon5001@gmail.com'
    email['subject'] = 'Checking code'
    email.set_content(html.substitute({'name': 'Roger'}), 'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as emailer:
        emailer.ehlo()
        emailer.starttls()
        emailer.login('learningpythonproject28@gmail.com', 'niharkajla12345')
        emailer.send_message(email)

    print('Email sent')