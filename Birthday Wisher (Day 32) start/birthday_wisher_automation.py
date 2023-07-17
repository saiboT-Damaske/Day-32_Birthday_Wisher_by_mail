##################### Extra Hard Starting Project ######################
import random
import smtplib
import pandas
import datetime as dt
import os

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
birthdays = pandas.read_csv("./birthdays.csv")

todays_day = dt.datetime.now().day
todays_month = dt.datetime.now().month

for (index, row) in birthdays.iterrows():
    if row.day == todays_day and row.month == todays_month:
        print("match found")
        birthday_person = row


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

r_letter = random.choice(os.listdir("./letter_templates"))

with open(f"./letter_templates/{r_letter}", "r") as letter:
    text = letter.read()

personalized_birthday_text = text.replace("[NAME]", birthday_person[0])
print(text)


# 4. Send the letter generated in step 3 to that person's email address.
mail = "YOUR EMAIL"
password = "APP PASSWORD"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=mail, password=password)
    connection.sendmail(from_addr=mail, to_addrs=birthday_person.email,
                        msg=personalized_birthday_text)