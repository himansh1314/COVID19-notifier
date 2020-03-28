# COVID19-notifier
This project scrapes data of COVID19  cases in India and sends emails at time to time basis.
Requirements:
Requires BeautifulSoup library to be installed
You can do so by typing ```pip install beautifulsoup4``` in your command line.
Command line arguments:
```
--emails: Path to text file where all the emails are stored
--loginid: Email id through which you would like to send the mails
--password: Password of the corresponding ID. NOTE: GMail requires App Specific password
--frequency: Time in minutes for sending email notifications.
```
Whenever you're done sending the emails, kindly quit the program using Keyboard Interrupt ```Ctrl+C``` so that SMTP server can be disconnected.
For adding the email ids in the text file, please enter different ids at different lines, as that is the required format.
