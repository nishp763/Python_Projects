import smtplib, ssl

def send_email(recv_email_addr, subj_line, msg_body):
    port = 465  # SSL
    sender_email = "myemail@gmail.com" # sender email address
    sender_password = "myemailpassword" # sender email password

    # Create a secure SSL context
    context = ssl.create_default_context()
    # Construct the message format
    message = "Subject: {}\n\n{}".format(subj_line, msg_body)

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, sender_password) # login into the server
        server.sendmail(sender_email, recv_email_addr, message) # send email

if __name__ == "__main__":
    recv_email_addr = "receveremail@gmail.com"
    subject_line = "Python: Hello Email!"
    message_body = "Hi, this is an email from Python program."
    send_email(recv_email_addr, subject_line, message_body)