import requests
from bs4 import BeautifulSoup
import smtplib
import os

MY_EMAIL = os.environ['GmailID']
MY_PASSWORD = os.environ['Gmail_Password']

URL = "https://www.amazon.in/Muji-Point-Black-0-38mm-Japan/dp/B01N8QNC59/ref=sr_1_1?dchild=1&keywords=muji&qid=1609431990&sr=8-1"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"
}
response = requests.get(URL, headers=headers )
# print(response.text)
webpage = response.text
soup = BeautifulSoup(webpage,"html.parser")
# print(soup.prettify())

#priceblock_ourprice
price_tag = soup.find(name="span", id="priceblock_ourprice")
price = float(price_tag.text.split()[1])

target_price = 700

#productTitle
title_tag = soup.find(name="span", id="productTitle")
title = title_tag.text.strip()
# print(title)

mail_message = f"Subject:Amazon item Price Drop 👆\n\nThe Item: {title} \nis now available at Rs.{price}\n{URL}"
mail_message_encoded = mail_message.encode(encoding='UTF-8',errors='strict')

if price <= target_price:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="csendranshi@gmail.com",
        msg=mail_message_encoded
    )