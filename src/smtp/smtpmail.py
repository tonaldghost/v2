import os
import smtplib
from email.message import EmailMessage

#hidden email variables
EMAIL_ADDRESS = os.environ.get('SMTPEMAIL')
EMAIL_PASS = os.environ.get('SMTPPASS')

def account_mail_sender(client, email_type):

    #!!
    #throw error if user passes anything
    #other than confirmation, otp or forgot_password as the email type.

    #client
    email_recipient = client

    #applying subject and html template to send to client based on email_type
    if email_type == "confirmation":
        with open('smtp/email_templates/confirmation.html', 'r', encoding='utf-8') as file:
            to_send = file.read()
            subject = 'Confirmation Email'
    elif email_type == "otp":
        with open('smtp/email_templates/otp.html', 'r', encoding='utf-8') as file:
            to_send = file.read()
            subject = 'OTP Email'
    if email_type == "forgot_password":
        with open('smtp/email_templates/forgot_password.html', 'r', encoding='utf-8') as file:
            to_send = file.read()
            subject = 'Forgot Password Email'

    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email_recipient
    msg['Subject'] = subject
    msg.set_content(to_send, subtype="html")

    #due to using the SSL connection there is no need no for 
    #extended hello func like ehlo() - now is secure from the start (port changes from ehlo 587 to ssl 465)
   
    # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #     smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
    #     smtp.send_message(msg)
    #     smtp.quit()
    print("COMMENTED OUT BUT MESSAGE SENT")


#*****************************
#LOCAL DEBUG SMTP FOR THE DEVS
#*****************************

# with smtplib.SMTP('localhost', 1025) as smtp:
#     subject = 'subject'
#     body = 'body'

#     #format email without any need for modules
#     msg = f'Subject: {subject}\n\n{body}'

#     smtp.sendmail(EMAIL_ADDRESS, 'tony.duchars@gmail.com', msg)
#     print("************")
#     print("DEBUG SENT")
#     print("************")


