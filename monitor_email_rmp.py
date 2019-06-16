#to download webpage for BeautifulSoup to parse
import requests

#BeautifulSoup will parse through webpage and search for keywords, phrases, html tags, etc.
from bs4 import BeautifulSoup

#time library will be used to check webpage for updates
import time

#smtplib for email functionality
import smtplib

while True:
    #set webpage to scrape
    url = "http://google.com"
    
    #headers
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    
    #note: if using macOS, you may need to install the lxml library -> python3 -m pip install lxml
    soup = BeautifulSoup(response.text, "lxml")

    #if keyword not found then check agian in 60 seconds
    if str(soup).find("Google") == -1: #here we pass find() the keyword we are looking for
        time.sleep(60)      
        continue
    #if keyword is found, a message is sent using smtplib to specified reciepients from your email
    else:
        msg = 'Subject: This is the send_scrap script, check WEBSITE!'
        fromaddr = 'YOUR EMAIL'
        toaddrs = ['RECIPIENT ONE EMAIL', 'RECIPIENT TWO EMAIL']

        # setup the email server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        #add my account login name and password
        server.login('YOUR EMAIL', 'YOUR EMAIL PSWRD')

        #print email's contents
        print('From: ' + fromaddr)
        print("To: " + str(toaddrs))
        print('Message: ' + msg)

        #send email
        server.sendmail(fromaddr, toaddrs, msg)

        #disconnect
        server.quit()

        
        break
