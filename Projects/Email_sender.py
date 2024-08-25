"""
Sends an email using the Gmail SMTP server.

This script sends an email to the email_reciever from the email_sender
using the Gmail SMTP server. The email's subject is set to "New Test Run"
and the body is a multi-line string with a small message about
Computer Science.

The email is sent over an SSL connection to the Gmail SMTP server at
port 465.

The email_sender and email_password variables must be set to the
email address and password of the Gmail account that will be used to
send the email.

The email_reciever variable must be set to the email address of the
recipient of the email.

"""


from email.message import EmailMessage #for the email object
import ssl #ssl is an encryption protocol
import smtplib 
#The Simple Mail Transfer Protocol (SMTP) is an Internet standard 
#communication protocol for electronic mail transmission.

email_sender = 'aimo.malik77@gmail.com'
email_password = 'mwtryisenjwgshsc' #generate app password from sender's gmail account

email_reciever = 'jacanor574@bymercy.com' #temporary mail
subject = "New Test Run "
body = """Hi there. 
    Computer Science is the study of computers and the methods and processes involved with computers.
    Computer feild is like the child class of Physics and Mathematics.
        I love Computer Science, especially programming.

                                    Regards, 
                                    Your self help team"""

em = EmailMessage() #instanciating an email message
em['From'] = email_sender #passing values to keys
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp: #465 is a port number used for email communication
	smtp.login(email_sender, email_password) #password will be used by smtp to login to sender's email account
	smtp.sendmail(email_sender, email_reciever, em.as_string())
