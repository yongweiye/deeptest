# coding = utf-8
# 发送html格式的邮件

import smtplib

from email.mime.text import MIMEText
from email.header import Header

if __name__ == "__main__":
    print("发送HTML邮件示例")

    # 邮件发送者
    sender = "sender@163.com"

    # 邮件接收地址列表
    receivers = "receiver@163.com"

    # html标识发送内容为文本格式
    msg = MIMEText("<p>微信公众号：开源优测</p><a href='http://www.testingunion.com'>开源优测社区</a>", "html", "utf-8")
    msg["From"] = "sender@163.com"
    msg["To"] = receivers

    # 构建邮件标题
    msg["Subject"] = Header("发送HTML格式邮件", "utf-8")

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
    print("登录结果:", log)

    # 发送邮件
    print(receivers)
    res = smtp.sendmail(sender, receivers, msg.as_string())
    print("邮件发送结果:", res)

    # 退出
    smtp.quit()
    print("send email finish")