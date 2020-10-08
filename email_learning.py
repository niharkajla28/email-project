import smtplib
from email.message import EmailMessage

if __name__ == '__main__':
    email = EmailMessage()
    email['from'] = 'Robot Guru'
    email['to'] = 'niharamazon5001@gmail.com'
    email['subject'] = 'Testing the python script project'
    email.set_content('I wanted to check if this works for our project which will help us to grow. Thanks for sharing')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as emailer:
        emailer.ehlo()
        emailer.starttls()
        emailer.login('learningpythonproject28@gmail.com', 'niharkajla12345')
        emailer.send_message(email)

        print('email sent')
