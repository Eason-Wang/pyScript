#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Eason Wang
# Contact: wangyishuai007@gmail.com
#
# Date: 2015.12.07
# Ver: 1.0
# Use: 
#	1. This script used in the Nagios Server;
#	2. This script needs to call check_ncpa.py, so to download check_ncpa.py script and put /usr/local/nagios/libexec(To change the directory location, modify the variable damon);
#	3. This script also need to be monitored have view_date.py script under your NCPA Plugin directory;
#	4. Run scripts: check_date.py -H <ncpaserver> -t <token>
#
# Exit code: 
# 0 ==> EXIT_SUCCESS
# 1 ==> EXIT_WARING
# 2 ==> EXIT_CRITICAL
# 3 ==> EXIT_UNKNOW

import os,sys,time,commands,getopt

def check_date(RIP,token):
    a,b = commands.getstatusoutput('/usr/local/nagios/libexec/check_ncpa.py -H %s -t %s -M agent/plugin/view_date.py' % (RIP,token))
    if a != 0: 
        return "[ERROR] check_ncpa.py Fails.(IP: %s)" % RIP
    if b == time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(time.time())):
        return "%s date is ok" % RIP
        sys.exit(0)
    else:
        return "%s date is cri" % RIP
        sys.exit(2)


if __name__ == "__main__":
    daemon = '/usr/local/nagios/libexec/check_ncpa.py'
    if not os.path.exists(daemon):
        print "[ERROR]check_ncpa.py file does not exist!"
        sys.exit(0)
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'H:t:')
    except getopt.GetoptError, e:
        print e
        sys.exit(0)

    RIP = ''
    token = ''
    if not opts:
        print "[ERROR]Please input parameters!"
    for i in opts:
        if '-H' in i:
            RIP = i[1]
        elif '-t' in i:
            token = i[1]
 
    if RIP and token:
        print check_date(RIP,token)
    else:
        print "[ERROR] Parameter error!\ncheck_date.py -H <ncpaserver> -t <token>"
    
