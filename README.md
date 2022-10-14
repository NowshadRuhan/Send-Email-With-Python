# Send-Email-With-Python
## Send Email With Python


## Run this code
```
import smtplib

myemail = "tester.new1996@gmail.com" #To email
password = "******************" #APP password

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user = "tester.new1996@gmail.com", password = password)

connection.sendmail(from_addr = myemail, to_addrs = "nowshad.cse@gmail.com", msg = "This is a Test email!")

connection.close()
```

### After setup this code, you need to setup APP password. 
```
1. Turn on 2-step Verification
```
```
2. Setup an app passwords
```


![G.your-QR-Code](https://github.com/NowshadRuhan/QR-Code-With-Python/blob/main/QRCode1.png?raw=true) 
