import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer,rating, comments):
    port=2525
    smtp_server = 'sandbox.smtp.mailtrap.io'
    login = '0726738d2236bf'
    password = '6a3b5db68ab931'
    message = f'<h3>New feedback submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>'
    sender_mail = 'mail1@example.com'
    reciever_mail = 'mail2@example.com'
    msg=MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_mail
    msg['To'] = reciever_mail
    with smtplib.SMTP(smtp_server,port) as server:
        server.login(login, password)
        server.sendmail(sender_mail, reciever_mail, msg.as_string())