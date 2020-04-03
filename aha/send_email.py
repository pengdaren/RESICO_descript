import smtplib
from email import message
from email import utils

email_fromaddr = 'chun.peng1@qq.com'
email_psw = 'ehddbxzmegdydfid'
email_conn = smtplib.SMTP_SSL('smtp.qq.com', 465)
email_conn.set_debuglevel(1)
email_conn.login(email_fromaddr, email_psw)
email_info = message.EmailMessage()
email_info.set_content('hello world', 'UTF-8')
email_info['subject'] = '假装有一个主题'
email_info['from'] = 'q.qchun<%s>' % email_fromaddr
email_info['to'] = 'recochun<%s>' % 'chun.peng@resico.cn'
email_conn.sendmail(email_fromaddr, ['chun.peng@resico.cn'], email_info.as_string())
email_conn.quit()
