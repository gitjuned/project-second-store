import smtplib, ssl

def sendmsg(msg):
    port = 465 #587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "yourmailhere@gmail.com"
    receiver_email = "yourmailhere@gmail.com"
    password = "password here"
    title = "Book Buddy Contact Us Form"
    message = "Subject:" + title + "\n" + msg
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        # server.ehlo()  # Can be omitted
        #server.startssl(context=context)
        # server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

