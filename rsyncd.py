#!/usr/bin/env python
# chkconfig: 35 24 96
#
# Author: Eason Wang
# Contact: wangyishuai007@gmail.com
#
# Date: 2015.11.10
# Ver: 1.0
# Use: 
#	cp rsyncd.py /etc/init.d/rsyncd
#	chkconfig --add rsyncd
#	service rsyncd [start|stop|restart|reload]
# Config: /etc/rsyncd/rsyncd.conf
#
# Exit code: 
# 0 ==> EXIT_SUCCESS
# 1 ==> EXIT_FAILURE

import sys,os,commands,getopt,signal

rsync = '/usr/bin/rsync'
CFILE = '/etc/rsyncd/rsyncd.conf'
PFILE = '/var/run/rsyncd.pid'
prog = 'rsync'

daemon = "%s --daemon --config=%s" % (rsync,CFILE)
PROCESS = os.popen("ps -ef | grep rsync | grep -v 'grep' | awk '{print $2}'").read().split('\n')[0]
if os.path.exists(PFILE):
    RPFILE = open(PFILE).read().strip()
else:
    RPFILE = ''

def start():
    if not os.path.exists(rsync):
        print "FATAL: No such programme"
        sys.exit(1)
    if not os.path.exists(CFILE):
        print "FATAL: config file does not exist"
        sys.exit(1)
    print "start %s:" % prog
    if os.path.exists(PFILE): 
        if PROCESS == RPFILE:
            print "%s is runing!" % prog
        else:
            try:
                os.remove(PFILE)
            except:
                print "[ERROR] pid file Delete failed, Please check!"
            else:
                print "Delete the pid file..."
                start()
    else :
        a,b = commands.getstatusoutput(daemon)
        if a !=0 :
            print b
            sys.exit(1)
        print "[OK]"

def stop():
    print "stop %s:" % prog
    try:
        os.kill(int(RPFILE), signal.SIGKILL)
    except (IOError, ValueError):
        print "%s is not runing!" % prog
    else:
        if os.path.exists(PFILE):
            try:
                os.remove(PFILE)
            except:
                print "[ERROR] pid file Delete failed, Please check!"
            else:
                print "Delete the pid file..."
                stop()
        else:
            print "[OK]"




if __name__ == '__main__':
    arg = sys.argv[1:]
    if len(sys.argv[1:]) > 1:
        print "Too many arguments! Only one!"
        sys.exit(0)
    if not arg : 
        print "You must enter parameters!"
        sys.exit(0)

    if 'start' in arg: 
        start()
        sys.exit(0)
    elif 'stop' in arg: 
        stop()
        sys.exit(0)
    elif 'restart' in arg or 'reload' in arg:
        stop()
        start()
        sys.exit(0)
    else:
        print "only supports the following parameters: [start|stop|restart|reload]"

    
