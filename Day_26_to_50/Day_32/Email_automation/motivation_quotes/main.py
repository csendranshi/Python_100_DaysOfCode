import datetime as dt
import random
import smtplib

my_email = "[your email_id]"
password = "[your password]"

now = dt.datetime.now()
now_week_day = now.weekday()
print(now_week_day)
if now_week_day == 0:

    with open('quotes.txt', encoding='utf8') as file:
        data = file.readlines()
        quote = random.choice(data)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="replyanshikagupta@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{quote}".encode('utf-8')
        )
