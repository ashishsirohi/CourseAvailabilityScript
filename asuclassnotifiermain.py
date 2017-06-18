import sys, os
import psycopg2
from ClassAvailability import check_status
from threading import Thread
from sendnotification import send_notification

#connect to databse
def getOpenConnection(user='admin', password='postgres', dbname='asuca'):
    return psycopg2.connect("dbname='" + dbname + "' user='" + user + "' host='localhost' password='" + password + "'")

def main():
    con = getOpenConnection()
    cur = con.cursor()
    cur.execute("select courseid, term from asuca_courses")
    result = cur.fetchall()
    exec_threads(result)

def exec_threads(result):
    for x in range(len(result)):
        status = check_status(result[x][0], result[x][1])
        if len(status) > 0 and status[2] > 0:
            con = getOpenConnection()
            cur = con.cursor()
            print "%s seats Available for %s by Prof. %s" % (status[2], status[1], status[0])
            emails = []
            cur.execute("select users from asuca_courses where courseid=" + str(result[3][0]))
            users = cur.fetchall()
            for x in users[0][0]:
                cur.execute("select emailid from asuca_userinfo where id=" + str(x))
                email = cur.fetchall()
                emails.append(email[0][0])
            #send_notification(emails, status)
        else:
            print "No seat available for %s" % str(result[x][0])




if __name__=="__main__":
    main()