#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Eason Wang
# Contact: wangyishuai007@gmail.com
#
# Date: 2015.11.20
# Ver: 1.0
# Use: 
#       1. change list_file(Need to check the ip list file)\date_command(Time Format) variable;
#       2. change your subject\receivers\sender\passwd\host(smtp server) in sendmail();
#       3. Receive e-mail default format:
#		subject: date status
#		body: 	192.168.1.161\t2015.11.20_11:25:18\n192.168.1.162\t2015.11.20_11:36:56\n192.168.1.163\t2015.11.20_11:41:58
#
# Exit code: 
# 0 ==> EXIT_SUCCESS
# 1 ==> EXIT_FAILURE

import os,sys,datetime,commands,smtplib
from email.mime.text import MIMEText


list_file = "/tmp/ip_list.txt"
date_command = 'date +%Y.%m.%d_%H:%M:%S'
date_list = []

def sendmail(bd):
    subject = 'date status'
    receivers = ["receivers@mail.com"]
    host = 'smtp.sendmail.com'
    port = 465    # If not SSL, modify (mark 1) 
    sender = 'sender@sendmail.com'
    passwd = "password"
    body = bd
    msg = MIMEText(body)
    msg['subject'] = subject
    msg['from'] = sender
    msg['to'] = ','.join(receivers)
    try:
        s = smtplib.SMTP_SSL(host, port) # mark 1
        s.login(sender, passwd)
        s.sendmail(sender, receivers, msg.as_string())
    except:
        print "Error: unable to send email"

if not os.path.exists(list_file):
    print "%s is not exits!" % list_file
    sys.exit(1)
with open(list_file) as f:
    list_data = f.readlines()


for ip in list_data:
    a,b = commands.getstatusoutput('ssh %s %s' % (ip.strip(),date_command))
    if a != 0:
        print "FATAL: Remote acquisition failure"
        sys.exit(1)
    else:
        date_list.append(ip.strip()+"\t"+b+"\n")

sendmail(''.join(date_list))
