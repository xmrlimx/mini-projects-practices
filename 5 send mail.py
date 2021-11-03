import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail_id = 'it.lim06@gmail.com'
mail_pass = 'Limproghe99'
to = ['xmrlimx@gmail.com', 'lim.hao@navigosgroup.com']
subject = 'Send test mail using Python'
body = """
Nếu một ngày em lỡ khóc sướt mướt chẳng thể dỗ dành, thì xin ai kia hãy khóc với những cảm thông của chính mình. Em sẽ ngừng khóc, em sẽ cười thôi, vì người tôi yêu giận dỗi nên mít ướt như vậy thôi!
"""

msg = MIMEMultipart()
msg["From"] = mail_id
msg["To"] = ', '.join(to)
msg["Subject"] = subject
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(mail_id, mail_pass)
text = msg.as_string()
server.sendmail(mail_id, to, text)
server.quit()

