# coding=utf-8
from email.mime.text import MIMEText
from email.header import Header
import smtplib
'''
sender = receiver = "zhzxweijing@126.com"

msg = MIMEText("<p>微信公众号号：开源优测</p><a href='http://www.testingunion.com'>开源优测社区</a>>"
               , "html", "utf-8")
msg["from"] = sender
msg["to"] = receiver

msg["subject"] = Header("deeptest", "utf-8")

smtpserver = "smtp.126.com"
smtpport = 25

smtp = smtplib.SMTP()
con = smtp.connect(smtpserver, smtpport)
print con

log=smtp.login(user="zhzxweijing@126.com",password="weiye13469619523")

print log

res=smtp.sendmail(sender,receiver,msg.as_string())
print res
smtp.close()
smtp.quit()
print res

'''

