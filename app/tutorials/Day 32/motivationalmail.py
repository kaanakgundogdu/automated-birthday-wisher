import smtplib
import random
import datetime as dt

gmail_my_email = "firsttestacc08@gmail.com"
gmail_password = "qftqjedijnvtlurj"
gmail_protocol = "smtp.gmail.com"

yahoo_email = "secondtest.acc@yahoo.com"
yahoo_password = "wooqlvjidytrokak"
yahoo_protocol = "smtp.mail.yahoo.com"

current_time = dt.datetime.now()
print(current_time.weekday())
if current_time.weekday() == 5:

    with open("app/tutorials/Day 32/quotes.txt", "r") as quotes_file:
        quotes = quotes_file.readlines()
        with smtplib.SMTP(yahoo_protocol, port=587) as connection:
            connection.starttls()
            connection.login(user=yahoo_email, password=yahoo_password)
            connection.sendmail(from_addr=yahoo_email, to_addrs=gmail_my_email,
                                msg=f"Subject:Monday Quotes\n\n{random.choice(quotes)}.")
