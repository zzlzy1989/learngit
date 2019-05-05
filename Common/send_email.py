# -*- coding: utf-8 -*-
# @Time : 2019年5月5日14:35:38
# @Author : GaoXu
# @File : send_email.py
# @Software: PyCharm

#简单的邮件传输协议
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class Send_Email():

    def __init__(self):
        #设置邮箱域名
        self.HOST = 'smtp.qq.com'
        #设置邮箱标题
        self.SUBJECT = 'CSDN First Blog'
        # 设置发件人邮箱
        self.FROM = '394845369@qq.com'
        #邮箱密码
        self.PASSWORD=''
        # 设置收件人邮箱
        self.TO = '394845369@qq.com'
        self.message = MIMEMultipart('related')

    def send_email_html(self):

        #message = MIMEMultipart('related')
        # 发送邮件主体到对方的邮箱中
        message_html = MIMEText('<h2 style="color:red;font-size:100px">CSDN博客超级好</h2><img src="cid:big">', 'html',
                                'utf-8')
        self.message.attach(message_html)
        print("message_html:{}".format(message_html))

    def send_email_image(self):
        #rb 读取二进制文件
        #确定有1.jpg这个文件
        image_data=open('F:\learngit\Image\scj_1.jpg','rb')
        #设置读取的二进制数据
        message_image=MIMEImage(image_data.read())
        #关闭刚才打开的资源文件
        image_data.close()
        message_image.add_header('Content-ID','big')
        #添加图片文件到邮件信息当中去
        message_image.attach(message_image)


    def send_email_files(self):
        #邮件中添加文件
        #确定当前目录中存在
        message_docx=MIMEText(open('F:\learngit\FIles\email_test.docx','rb').read(),'base64','utf-8')
        #设置文件在附件当中的名字
        message_docx['Content-Disposition'] = 'attachment;filename="email_test.docx"'
        self.message.attach(email_test.docx)

        #设置邮件发送人
        self.message['From'] = self.FROM
        # 设置邮件收件人
        self.message['To'] = self.TO
        # 设置邮件标题
        self.message['Subject'] = self.SUBJECT

        # 获取简单邮件传输协议的证书
        email_client = smtplib.SMTP_SSL()
        # 设置发件人邮箱的域名和端口，端口为465
        email_client.connect(self.HOST, '465')
        # ---------------------------邮箱授权码------------------------------
        result = email_client.login(self.FROM, self.PASSWORD)
        print('登录结果', result)
        email_client.sendmail(from_addr=self.FROM, to_addrs=self.TO.split(','), msg=self.message.as_string())
        # 关闭邮件发送客户端
        email_client.close()

if __name__ == '__main__':
    send_email  = Send_Email()
    send_email.send_email_html()
#    send_email.send_email_image()
#    send_email.send_email_files()