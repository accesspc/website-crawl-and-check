import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email():

    def __init__(self, config) -> None:
        self.sender = config['sender']
        self.recipients = ', '.join(config['recipients'])
        self.server = config['server']

        self.msgs = config['msg']

    def __send(self, web):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = '{} is {}!'.format(
            web['website'],
            self.msg['status']
        )
        msg['From'] = self.sender
        msg['To'] = self.recipients

        with open('templates/email.html', 'r') as feh:
            html = feh.read().format(
                msg_h1_color=self.msg['h1_color'],
                msg_h1=self.msg['h1'],
                response=web['response'],
                status=web['status'],
                timestamp=web['timestamp'],
                website=web['website'],
            )

        with open('templates/email.txt', 'r') as fet:
            text = fet.read().format(
                msg_h1=self.msg['h1'],
                response=web['response'],
                status=web['status'],
                timestamp=web['timestamp'],
                website=web['website'],
            )

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        msg.attach(part1)
        msg.attach(part2)

        try:
            with smtplib.SMTP(self.server) as s:
                s.send_message(msg)
                s.quit()
        except smtplib.SMTPResponseException as errs:
            return 'SMTP Error: {}'.format(errs)
        except Exception as err:
            return 'Exception: {}'.format(err)

        return 'Message sent'

    def sendOk(self, web):
        self.msg = self.msgs['ok']

        return self.__send(web)

    def sendWarn(self, web):
        self.msg = self.msgs['warn']

        return self.__send(web)
