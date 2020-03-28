# -*- coding: utf-8 -*-
#importing the libraries
import requests
import bs4
import smtplib
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--emails", required = True, help = "Location of the text file where email ids are stored")
parser.add_argument("--loginid", required = True, help = "Login id from sending email")
parser.add_argument("--password", required = True, help = "Corresponding password")
parser.add_argument("--frequency", required = True, help = "Frequency of sending emails in minutes")
args = parser.parse_args()

def load_ids(path):
    """
    This function loads all the email ids given in a text file and returns a list containing all
    email ids.
    Arguments: path to text file
    Returns: List containing email ids
    """
    users = open(path, 'r')
    list1 = []
    for line in users:
        list1.append(line)
    for i in range(0,len(list1)-1):
        list1[i] = list1[i][:-1]
    return list1
    
def login(userID, password):
    """
    This function initialises SMTP and logs in to email id credentials provided by the user.
    Arguments
    userID: email ID 
    password: valid password for the email ID. For Gmail, app specific password may be required.
    Returns smtp object which will be used to send emails in the send_emails function.
    """
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    except Exception:
        print('Please connect to internet')
    
    smtpObj.ehlo()
    smtpObj.starttls()
    
    try:
        smtpObj.login(userID, password)
    except Exception:
        print('Incorrect login credentials')
    return smtpObj

def send_emails(loaded_ids, smtpObj, frequency, loginID):
    try:
        while True:
            res = requests.get('https://www.mygov.in/covid-19/')
            ids = loaded_ids
            
            try:
                res.raise_for_status()
            except Exception:
                print('There was a problem loading the page '.format(Exception))
                  
            soup = bs4.BeautifulSoup(res.text, "html.parser")
            count = soup.select('div span[class="icount"]')
            message = 'Passengers screened at airport {} \nActive COVID-19 Cases {} \nCured cases {} \nDeath cases {} \nThe data provided here has been sourced from https://www.mygov.in/covid-19/. \nTake care and stay at home'.format(count[0].getText(), count[1].getText(), count[2].getText(), count[3].getText())
            email = 'Subject: COVID-19 Updates\n' + message
            smtpObj.sendmail(loginID, ids, email)
            print('email sent')
            time.sleep(frequency*60)
    except KeyboardInterrupt:
        print("Logging out...")
        smtpObj.quit()
    
loaded_ids = load_ids(args.emails)
smtp = login(args.loginid, args.password)
send_emails(loaded_ids, smtp, float(args.frequency), args.loginid)

