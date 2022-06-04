import smtplib


gmail_my_email = "firsttestacc08@gmail.com"
gmail_password = "qftqjedijnvtlurj"
gmail_protocol = "smtp.gmail.com"

yahoo_email = "secondtest.acc@yahoo.com"
yahoo_password = "wooqlvjidytrokak"
yahoo_protocol = "smtp.mail.yahoo.com"


with smtplib.SMTP(yahoo_protocol, port=587) as connection:
    connection.starttls()
    connection.login(user=yahoo_email, password=yahoo_password)
    connection.sendmail(from_addr=yahoo_email, to_addrs=gmail_my_email,
                        msg="Subject:Hello\n\nThis is the body of my email. Mic check one two.")
