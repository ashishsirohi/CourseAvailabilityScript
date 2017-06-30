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
    #exec_threads(result)
    threads = []
    for th in range(len(result)):
        t = Thread(target=exec_threads, args=(result[th][0], result[th][1]))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

def exec_threads(course, term):
    status = check_status(course, term)
    if len(status) > 0 and status[2] > 0:
        con = getOpenConnection()
        cur = con.cursor()
        name = str(status[1]).replace('\n', '')
        name2 = name.replace('\t', '')
        print "%s seats Available for %s by Prof. %s \n" % (status[2], name2, status[0])
        emails = []
        cur.execute("select users from asuca_courses where courseid=" + str(course))
        users = cur.fetchall()
        for x in users[0][0]:
            query = "select emailid from asuca_userinfo where username = '"+(str(x))+"'"
            cur.execute(query)
            email = cur.fetchall()
            emails.append(email[0][0])
        send_notification(emails, status, term, name2, course)
    else:
        print "No seat available for %s \n" % str(course)


def run():
    count = 0
    while(1):
        main()
        count = count + 1
        print count


if __name__=="__main__":
    run()