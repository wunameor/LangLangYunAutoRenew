import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import fileUtils

email_url = "./config/email/main.json"
data = fileUtils.toJson(email_url)

# 创建带附件的邮件


# 添加附件（可选）
# with open("attachment.txt", "rb") as f:
#     part = MIMEApplication(f.read(), Name="attachment.txt")
#     part["Content-Disposition"] = 'attachment; filename="attachment.txt"'
#     msg.attach(part)

def send(fromEmail, toEmail, subject, body):
    try:
        msg = MIMEMultipart()
        msg["From"] = fromEmail
        msg["To"] = toEmail
        msg["Subject"] = subject
        # 使用传入的 body 作为正文
        msg.attach(MIMEText(body, "plain"))
        server = smtplib.SMTP_SSL(data["smtp_server"], data["smtp_port"])  # SSL 加密连接
        server.login(fromEmail, data["sender_password"])
        # 收件人改为列表格式，使用 msg.as_string() 生成邮件内容
        server.sendmail(fromEmail, toEmail, msg.as_string())
        print("邮件发送成功！")
    except Exception as e:
        print(f"发送失败: {e}")
    finally:
        server.quit()

