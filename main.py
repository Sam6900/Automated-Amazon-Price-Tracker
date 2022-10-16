import requests
from bs4 import BeautifulSoup
import os
import smtplib

prod_url = "https://www.amazon.in/Lenovo-Ideapad-39-62cm-Keyboard-82K201UEIN/dp/B0B6GJH5Q7/ref=sr_1_4?keywords=Lenovo+Ideapad+Gaming+3&qid=1665856961&qu=eyJxc2MiOiI0LjkzIiwicXNhIjoiNC41MyIsInFzcCI6IjMuMTQifQ%3D%3D&s=computers&sr=1-4"
target_price = 51000
my_email = os.environ["MY_EMAIL"]
my_password = os.environ["MY_PASSWORD"]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.7"
}
response = requests.get(prod_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
prod_title_tag = soup.find(name="span", id="productTitle")
prod_title = prod_title_tag.getText().strip()[:100]
price_tag = soup.find(name="span", class_="a-price-whole")
price_amt = float(price_tag.getText().replace(",", ""))

if price_amt < target_price:
    message = f"{prod_title}.....  is now less than Rs.{target_price}. Buy now! \n{prod_url}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="sahilsharma220202004@gmail.com", msg=message)
