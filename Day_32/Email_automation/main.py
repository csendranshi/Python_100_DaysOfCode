import smtplib

my_email = "[your email_id]"
password="[you password]"

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="replyanshikagupta@gmail.com",
        msg="Subject: Testing\n\nHello World"
    )

# import datetime as dt
#
# now = dt.datetime.now()
# print(now.month)
#
# my_birthday = dt.datetime(year=2000,month=4,day=8,hour=4)
# print(my_birthday)