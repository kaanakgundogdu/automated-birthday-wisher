import smtplib

# YOU SHOULD WRITE YOUR OWN MAIL AND PASSWORD
# YOU SHOULD WRITE YOUR OWN MAIL AND PASSWORD
# YOU SHOULD WRITE YOUR OWN MAIL AND PASSWORD
gmail_my_email = "-------------------------@gmail.com"
gmail_password = "----------------------------------------"
gmail_protocol = "smtp.gmail.com"


# YOU SHOULD WRITE YOUR OWN MAIL AND PASSWORD
# YOU SHOULD WRITE YOUR OWN MAIL AND PASSWORD
# YOU SHOULD WRITE YOUR OWN MAIL AND PASSWORD
yahoo_email = "----------------------@yahoo.com"
yahoo_password = "----------------------"
yahoo_protocol = "smtp.mail.yahoo.com"


with smtplib.SMTP(yahoo_protocol, port=587) as connection:
    connection.starttls()
    connection.login(user=yahoo_email, password=yahoo_password)
    connection.sendmail(from_addr=yahoo_email, to_addrs=gmail_my_email,
                        msg="Subject:Hello\n\nThis is the body of my email. Mic check one two.")
