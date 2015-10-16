# Originally, this program was meant to send a random email from the arrays, every five minutes.
# The program was then edited to send a random email, at random time intervals less than one hour.
# This is, of course, only to be used as a prank, please don't abuse this.
# A very simple script made for fun, and to learn some basic python.
#
#
# Known bugs:
#	The program will have an unexpected server connection loss.

import smtplib
import time 
import random

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

user = "YOUR EMAIL"
pwd = "YOUR PASSWORD."

to = "FRIEND'S EMAIL"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(user, pwd)

subjectList = [
	
]

messageList = [
	
]

#index is used to determine which email to send, randomly.
#oldindex is used to make sure you don't send the same email twice.
index = random.randint(0, len(messageList) - 1)
oldindex = index

msg = MIMEMultipart()
msg['From'] = user
msg['To'] = to
msg['Subject'] = subjectList[index]
 
body = messageList[index]
msg.attach(MIMEText(body, 'plain'))

text = msg.as_string()
server.sendmail(user, to, text)
oldTime = time.time();


while True: # Of course I want this to run indefinitely. To exit, use your keyboard interrupt (CTRL+C here).
	randomTime = random.randint(1, 3600) # Picks a random time that's less than one hour.
	if time.time() - oldTime > randomTime:
		index = random.randint(0, len(messageList) - 1)
		if index == oldindex:
			flag = True
			while flag:
				index = random.randint(0,2)
				if index != oldindex:
					flag = False
					
		oldindex = index

		msg = MIMEMultipart()
		msg['From'] = user
		msg['To'] = to
		msg['Subject'] = subjectList[index]
 
		body = messageList[index]
		msg.attach(MIMEText(body, 'plain'))
		
		text = msg.as_string()
		server.login(user, pwd)
		server.sendmail(user, to, text)
		print("Message sent at " + time.strftime("%I:%M:%S"))
		
		oldTime = time.time();
	
	print "..."
	time.sleep(15)

