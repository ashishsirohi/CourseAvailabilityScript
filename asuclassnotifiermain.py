import sys
import os
import psycopg2
from ClassAvailability import check_status
from sendnotification import send_notification

#connect to databse
def getOpenConnection(user='admin', password='postgres', dbname='asuca'):
    return psycopg2.connect("dbname='" + dbname + "' user='" + user + "' host='localhost' password='" + password + "'")

def main():
    con = getOpenConnection()
    cur = con.cursor()
    cur.execute("Select courseid, term from asuca_courses")
    result = cur.fetchall()
    courses = []
    term = []
    #for x in range(len(result)):
     #   check_status(result[x][0], result[x][1])

    status = check_status(result[3][0], result[3][1])
    if status[2] > 0:
        print "Seat Available"
        send_notification()


if __name__=="__main__":
    main()