import sys
import os
import psycopg2
from classavailbility import check_status

#connect to databse
def getOpenConnection(user='admin', password='postgres', dbname='postgres'):
    return psycopg2.connect("dbname='" + dbname + "' user='" + user + "' host='localhost' password='" + password + "'")

def main():
    con = getOpenConnection()
    cur = con.cursor()
    cur.execute("Select courses from userinfo")

    pass


if __name__=="__main__":
    main()