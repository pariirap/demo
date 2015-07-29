from __future__ import with_statement
from multiprocessing import Process
from fabric.api import local, hosts, settings, abort, run, cd, env, put
from fabric.contrib.files import  exists
from fabric.contrib.console import confirm
import psycopg2
import datetime


#conn = psycopg2.connect("dbname='testdb' user='postgres' host='172.16.2.112' password='whatever'")

env.user='root'
env.warn_only=True
#env.hosts = ['172.16.3.122']

SwoopVM = ['172.16.2.120','172.16.2.121']
PostgresVM = ['172.16.2.121']
HAproxyVM = ['172.16.2.116', '172.16.2.117']
VIPVM = ['172.16.2.116', '172.16.2.117']



@hosts(PostgresVM)
def dbcon():
    try:

        print ("connection made")
        cur = conn.cursor()
        cur.execute("""SELECT * from company;""")
        rows = cur.fetchall()
        for row in rows:
            print "   ", row
    except:
        print "I am unable to connect to the database"



def createdb():
    pass

@hosts(SwoopVM)
def MonitorSwoop():
    try:
        status=run("service swoop status", warn_only=True)
        s  = status.split()
        #print ("s is ", s)
        if 'running...' in s:
            print ("SWOOPMONITOR %s Swoop server online %s" % (env.host,datetime.datetime.now().strftime("%Y-%m-%d %H:%M") ) )
        else:
            print ("SWOOPMONITOR %s Swoop server NOT online %s" % (env.host,datetime.datetime.now().strftime("%Y-%m-%d %H:%M") ) )
            status=run("service swoop start", warn_only=True)
            status=run("service swoop status", warn_only=True)
            s  = status.split()
            if 'running...' in s:
                print ("SWOOPMONITOR %s swoop server BACK online %s" % (env.host,datetime.datetime.now().strftime("%Y-%m-%d %H:%M") ) )



    except:
        print("SWOOPMONITOR *** %s VM DOWN ***  %s" % (env.host, datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))


@hosts(PostgresVM)
def MonitorPostgres():
    try:
        status=run("service postgresql-9.4 status", warn_only=True)
        s  = status.split()
        #print ("s is ", s)

        if 'running...' in s:
            print ("SWOOPMONITOR %s postgres server ONLINE %s" % (env.host,datetime.datetime.now().strftime("%Y-%m-%d %H:%M") ) )
        else:
            print ("SWOOPMONITOR %s postgres server DOWN %s" % (env.host,datetime.datetime.now().strftime("%Y-%m-%d %H:%M") ) )

            status=run("service postgresql-9.4 start", warn_only=True)
            status=run("service postgresql-9.4 status", warn_only=True)
            s  = status.split()
            if 'running...' in s:
                print ("SWOOPMONITOR %s postgres server BACK ONLINE %s" % (env.host,datetime.datetime.now().strftime("%Y-%m-%d %H:%M") ) )
    except:
        print("SWOOPMONITOR *** %s VM DOWN ***   %s" % (env.host,datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))


@hosts(PostgresVM)
def MonitorBackupPostgres():
    try:
        status=run("crontab -u postgres -l", warn_only=True)
        s  = status.split()
        #print ("s is ", s)
        if 'no' in s:
            print ("SWOOPMONITOR %s postgres BACKUP cron job DOWN %s" % (env.host,datetime.datetime.now().strftime("%Y-%m-%d %H:%M") ) )

        else:
            print ("SWOOPMONITOR %s postgres BACKUP cron job RUNNING %s" % (env.host,datetime.datetime.now().strftime("%Y-%m-%d %H:%M") ) )

    except:
        print("SWOOPMONITOR *** %s VM DOWN ***   %s" % (env.host, datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))

@hosts(HAproxyVM)
def MonitorHAproxy():
    try:
        status=run("service haproxy status", warn_only=True)
        s  = status.split()
        #print ("s is ", s)
        if 'running...' in s:
            print ("SWOOPMONITOR %s HAproxy server ONLINE %s" % (env.host,datetime.datetime.now().strftime("%Y-%m-%d %H:%M") ) )
        else:
            print ("SWOOPMONITOR %s HAproxy server DOWN %s" % (env.host,datetime.datetime.now().strftime("%Y-%m-%d %H:%M") ) )
            status=run("service haproxy start", warn_only=True)
            status=run("service haproxy status", warn_only=True)
            s  = status.split()
            if 'running...' in s:
                print ("SWOOPMONITOR %s HAproxy server BACK online %s" % (env.host,datetime.datetime.now().strftime("%Y-%m-%d %H:%M") ) )



    except:
        print("SWOOPMONITOR *** %s VM DOWN ***   %s" % (env.host, datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))

@hosts(VIPVM)
def MonitorVIP():
    try:
        status=run("service keepalived status", warn_only=True)
        s  = status.split()
        #print ("s is ", s)
        if 'running...' in s:
            print ("SWOOPMONITOR %s Keepalived server ONLINE %s" % (env.host,datetime.datetime.now().strftime("%Y-%m-%d %H:%M") ) )
        else:
            print ("SWOOPMONITOR %s Keepalived server NOT ONLINE %s" % (env.host,datetime.datetime.now().strftime("%Y-%m-%d %H:%M") ) )
            status=run("service keepalived start", warn_only=True)
            status=run("service keepalived status", warn_only=True)
            s  = status.split()
            if 'running...' in s:
                print ("SWOOPMONITOR %s keepalived server BACK ONLINE %s" % (env.host,datetime.datetime.now().strftime("%Y-%m-%d %H:%M") ) )
    except:
        print("SWOOPMONITOR *** %s VM DOWN ***   %s" % (env.host, datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))



def ignorethistesttask2():
    status=run("service haproxy status", warn_only=True)
    s  = status.split()
    #print ("s is ", s)
    r1 ="running..."
    if r1 in status:
        log("HAproxy is running")
        cur=conn.cursor()
        cur.execute("""INSERT INTO COMPANY (ID, NAME,AGE,ADDRESS,SALARY,JOIN_DATE) VALUES (6, 'Peter', 42, 'California', 120000.00 ,'2011-07-13');""")
        conn.commit()
    else:
        cur=conn.cursor()
        cur.execute("""INSERT INTO COMPANY (ID, NAME,AGE,ADDRESS,SALARY,JOIN_DATE) VALUES (99, 'STOP', 42, 'California', 120000.00 ,'2011-07-13');""")
        conn.commit()
        log(s[2])

def inputdb():
    for i in range(11,10000):
        cur=conn.cursor()
        cur.execute("""INSERT INTO COMPANY (ID, NAME,AGE,ADDRESS,SALARY,JOIN_DATE) VALUES (%s, 'DUMMY', 42, 'California', 120000.00 ,'2011-07-13');""", (i,))
        conn.commit()


def mail():
    #alert
    #this works os.system
    os.system("echo \"hi from python\" | mail -s subject pari@swoopsrch.com")

def log(msg):
    print(msg)


