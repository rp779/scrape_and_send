import requests
from bs4 import BeautifulSoup
import time
import smtplib

while True:
    url = "http://google.com"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")


    if str(soup).find("Google") == -1:
        time.sleep(60)
        continue
    else:
        msg = 'Subject: This is the rmp script, check rmp!'
        fromaddr = 'rparsons779@gmail.com'
        toaddrs = ['rparsons779@gmail.com']

        # setup the email server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        #add my account login name and password
        server.login('rparsons779@gmail.com', 'Florida32!')

        #print email's contents
        print('From: ' + fromaddr)
        print("To: " + str(toaddrs))
        print('Message: ' + msg)

        #send email
        server.sendmail(fromaddr, toaddrs, msg)

        #disconnect
        server.quit()

        break