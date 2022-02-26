import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
'''
   Note : 
        Create an account with SendGrid to use it .
        Generate and store a SendGrid API key and provide full access to Mail Send permissions.
 '''

def thanks_for_contacting_message(email, name):

    my_sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))           # -->API KEY here

    
    from_email = Email("your_email@example.com")                                             # -->Change to your verified sender
    to_email = To(email)                                                                     # --> Change to your recipient

    subject = "subject"
    content = Content(f"Thank you for your message {name.capitalize} ", "consectetur adipiscing elit")               # -->Thankyou message here

    mail = Mail(from_email, to_email, subject, content)

    mail_json = mail.get()                                                                   # --> Get a JSON-ready representation of the Mail object

  
    response = my_sg.client.mail.send.post(request_body=mail_json)                           # --> Send an HTTP POST request to /mail/send


#-------------------------------------------------------------
#We can also use SMTPLIB and trycourier module for sending mails