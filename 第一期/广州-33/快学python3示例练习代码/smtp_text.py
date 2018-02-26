# coding = utf-8
# 通过163邮箱发送纯文本邮件

import smtplib

from email.mime.text import MIMEText
from email.header import Header

if __name__ == "__main__":
    print("发送文本邮件示例")

    # 邮件发送者
    sender = "sender@163.com"

    # 邮件接收地址列表
    receivers = "receivers@163.com"

    # 发送内容构建
    # text标识发送内容为文本格式
    msg = MIMEText("SMTP发送文本邮件练习", "plain", "utf-8")
    msg["From"] = "sender@163.com"
    msg["To"] = receivers

    # 构建邮件标题
    msg["Subject"] = Header("SMTP发送文本邮件练习", "utf-8")

    # smtp服务
    smtpsever = "smtp.163.com"
    smtpport = 25

    # 发送人邮件用户名或专用于smtp账户用户名
    username = "username"

    # 发送人邮件密码或专用于smtp账户的密码
    password = "password"

    # 构建smtp对象
    smtp = smtplib.SMTP()

    # 连接到smtp服务
    con = smtp.connect(smtpsever, smtpport)
    print("连接结果:", con)

    # 登录smtp服务
    log = smtp.login(username, password)

    # 发送邮件
    print(receivers)
    res = smtp.sendmail(sender, receivers, msg.as_string())
    print("邮件发送结果:", res)

    # 退出
    smtp.quit()
    print("send email finish")