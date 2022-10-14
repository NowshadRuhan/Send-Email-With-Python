import smtplib

myemail = "tester.new1996@gmail.com" #To email
password = "*************" # APP password

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user = myemail, password = password)

connection.sendmail(from_addr = myemail, to_addrs = "nowshad.cse@gmail.com", msg = "This is a Test email!")

connection.close()