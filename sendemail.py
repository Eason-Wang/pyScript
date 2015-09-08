#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --2015.09.07--
# 脚本用来替换nagios监控发报警邮件
# sendemail.py 
# 方法：
# printf "邮件内容" | sendemail.py -s "邮件主题" -R 收件人1，收件人2
import smtplib,sys,random,getopt
from email.mime.text import MIMEText
def sendemail():
    subject = ''
    receivers = []
    sendlist = [('smtp.aliyun.com', 'atteam@aliyun.com'), ('smtp.sina.com', 'atteam_jk@sina.com'),  ('smtp.sina.cn', 'atteam@sina.cn'), ('smtp.qq.com', 'atteam_jk@foxmail.com')]
    rannum = random.randint(0, 3)
    host = sendlist[rannum][0]
    sender = sendlist[rannum][1]
    port = 465
    copyto = ['694101558@qq.com', '3759287@qq.com', '120359809@qq.com', '472945017@qq.com', '447768237@qq.com']
    passwd = 'xiaowang2013'
    #参数获取收件人
    try:
        opts, args = getopt.getopt(sys.argv[1:], 's:R:')
        for i in opts:
            if '-s' in i:
                subject = i[1]
            elif '-R' in i:
                receivers.append(i[1])
    except getopt.GetoptError, e:
        print e
    #以下代码段使用的MIMEText函数会生成邮件头格式，方便后边发送邮件时提供一些选项配置（object.sendmail方法）
    body = ''.join(sys.stdin.readlines())
    msg = MIMEText(body)
    msg['subject'] = subject
    msg['from'] = sender
    msg['to'] = ','.join(receivers)
    msg['cc'] = ','.join(copyto)
    receivers = receivers + copyto
    s = smtplib.SMTP_SSL(host, port)
    s.login(sender, passwd)
    s.sendmail(sender, receivers, msg.as_string())

count = 1
while count < 5:
    try:
        sendemail()
    except smtplib.SMTPSenderRefused:
        pass
    else:
        break
