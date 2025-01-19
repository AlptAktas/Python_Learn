import smtplib
import datetime as dt
import random

MY_EMAIL = "gilavoldinni@gmail.com"
MY_PASSWORD = "joxk ipyx vunv qnrg"

send_to = "gilavoldinni@hotmail.com"



now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("Day_32/Birthday Wisher/quotes.txt", "r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    
    print(quote)



with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL, 
        to_addrs=send_to, 
        msg=f"Subject:Tuesday Motivation\n\n{quote}"
    )