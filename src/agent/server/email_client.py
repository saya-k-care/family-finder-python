import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class AgentEmail:
    @staticmethod 
    def send_email(email_to, id, name):
        print ('Parameters email--> ', email_to, id, name)
#msg = email.message_from_string('warning')
        url = "https://eyebot.name.my/agent/view/" + str(id) + "/";
        msg = MIMEMultipart("alternative")
        msg['From'] = "matabotmin@outlook.com"
        msg['To'] = email_to
        msg['Subject'] = "EyeBot \"Unknown Person\" Replied from " + name

        text = """\
        Hi,
        Check out the replied from the unknown person:
        Click Here for the details?
        %s
    
        SMTP Server for Testing: Cloud-based or Local?
        https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server/

        Feel free to let us know what content would be useful for you!"""

        html = """\
        <html>
          <body>
            <p>Hi,<br>
              Check out the relied from the unknown person::</p>
            <p><a href="%s">Click Here for the details</a></p>
            <p> Feel free to <strong>let us</strong> know what content would be useful for you!!</p>
          
          <iframe 
                    width="425"
                    height="350"
                    frameborder="0"
                    scrolling="no"
                    marginheight="0"
                    marginwidth="0"
                    [src]="www.google.com"
          ></iframe>
          </body>
        </html>
    """

        text = text.replace("%s", url)
        print('test-->' + text)
        html = html.replace("%s", url)
    
# convert both parts to MIMEText objects and add them to the MIMEMultipart message
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        msg.attach(part1)
        msg.attach(part2)

        s = smtplib.SMTP("smtp-mail.outlook.com",587)
        s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
        s.starttls() #Puts connection to SMTP server in TLS mode
        s.ehlo()
        s.login('matabotmin@outlook.com', 'Eyebotmin0.')

        s.sendmail("admin@eye-bot.com", "pcyuen98@gmail.com", msg.as_string())

        s.quit()

    @staticmethod 
    def register_email(email_to, id):
        print ('Parameters email--> ', email_to, id)
#msg = email.message_from_string('warning')
        url = "https://eyebot.name.my/agent/update/" + str(id) + "/";
        msg = MIMEMultipart("alternative")
        msg['From'] = "matabotmin@outlook.com"
        msg['To'] = email_to
        msg['Subject'] = "MataBot New Registration"

        text = """\
            Hi Sir/Madam,
            Check out the generated text below for the unknown sender
            Click Here on how to use https://eyebot.name.my/how 
                Hi Sir/Madam, i may not available to reply your message now. If you are
            new to me, please fill up the form below and i will get back to you soonest possible
            %s
            """

        html = """\
        <html>
          <body>
            <p>Hi Sir/Madam,<br>
              Check out the generated text below for the unknown sender</p>
            <p>Click Here on how to use https://eyebot.name.my/how</p>
            <p>======================</p>
            <p>Hi Sir/Madam, i may not available to reply your message now. If you are
            new to me, please fill up the form below and i will get back to you soonest possible</p>
            <p>%s</p>
            <p>=====================</p>
          </body>
        </html>
    """

        text = text.replace("%s", url)
        
        html = html.replace("%s", url)
        print('test-->' + html)
# convert both parts to MIMEText objects and add them to the MIMEMultipart message
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        msg.attach(part1)
        msg.attach(part2)

        s = smtplib.SMTP("smtp-mail.outlook.com",587)
        s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
        s.starttls() #Puts connection to SMTP server in TLS mode
        s.ehlo()
        s.login('matabotmin@outlook.com', 'Eyebotmin0.')

        s.sendmail("admin@eye-bot.com", "pcyuen98@gmail.com", msg.as_string())

        s.quit()
        
def main(self):
    if __name__ == "__main__":
        print ('here')


AgentEmail().send_email('pcyuen98@gmail.com', '24', 'unknown')
#AgentEmail().register_email("pcyuen98@gmail.com", 12)
