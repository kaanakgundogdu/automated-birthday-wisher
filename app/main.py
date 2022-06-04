import pandas
import random
import datetime as dt
import smtplib

birthday_people_name = ""
birthday_people_email = ""
is_there_any_birthday = False

gmail_my_email = "firsttestacc08@gmail.com"
gmail_password = "qftqjedijnvtlurj"
gmail_protocol = "smtp.gmail.com"

current_time = dt.datetime.now()
curren_month = current_time.month
today = current_time.day

birthdays_data = pandas.read_csv("app/birthdays.csv")
birthday_dict = birthdays_data.to_dict()

for i in birthday_dict["month"]:

    if birthday_dict["month"][i] == curren_month:
        if birthday_dict["day"][i] == today:
            birthday_people_name = birthday_dict["name"][i]
            birthday_people_email = birthday_dict["email"][i]
            is_there_any_birthday = True

rand_file_index = random.randint(1, 3)


with open(f"app\letter_templates\letter_{rand_file_index}.txt", "r") as file:
    data = file.read().replace("[NAME]", birthday_people_name)
    with smtplib.SMTP(gmail_protocol, port=587) as connection:
        connection.starttls()
        connection.login(user=gmail_my_email, password=gmail_password)
        connection.sendmail(from_addr=gmail_my_email, to_addrs=birthday_people_email,
                            msg=f"Subject:Happy Birthday\n\n{data}.")
