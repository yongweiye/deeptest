# coding = utf-8
# 附件格式邮件

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

if __name__ == "__main__":
    print("发送附件邮件示例")
    # 邮件发送者
    sender = "sender@163.com"

    # 邮件接收地址列表
    receivers = "receiver@163.com"

    # 发送内容构建
    # html标识发送内容为文本格式
    msg = MIMEMultipart()
    msg["From"] = "sender@163.com"
    msg["To"] = receivers

    # 构建邮件标题
    msg["Subject"] = Header("附件格式邮件", "utf-8")

    # 构建邮件正文内容
    msg.attach(MIMEText("附件格式邮件", "plain", "utf-8"))

    # 构造附件
    attach1 = MIMEText(open("smtp_attach.py", 'rb').read(), "base64", "utf-8")
    attach1["Content-Type"] = "application/octet-stream"

    # filename会在邮件中显示
    attach1["Content-disposition"] = "attachment;filename=cody.py"

    # 关联附件到邮件中
    msg.attach(attach1)

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
    login = smtp.login(username, password)
    print("登录结果:", login)

    # 发送邮件
    print(receivers)
    res = smtp.sendmail(sender, receivers, msg.as_string())
    print("邮件发送结果:", res)

    # 退出
    smtp.quit()

    print("send email finish")