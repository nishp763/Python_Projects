def send_email(recv_email_addr, subj_line, msg_body):
    print(recv_email_addr)
    print(subj_line)
    print(msg_body)

if __name__ == "__main__":
    recv_email_addr = "nishp763@gmail.com"
    subject_line = "Python: Hello Email!"
    message_body = "Hi, this is an email from Python program."
    send_email(recv_email_addr, subject_line, message_body)