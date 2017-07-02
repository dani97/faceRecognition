import mysql.connector as mariadb
from mysql.connector.cursor import MySQLCursorPrepared
class DBAccess:

    def __init__(self):
        self.db = mariadb.connect(host = "127.0.0.1",user = "root",password= "",database ="aafr", port = 3306)
        self.cursor = self.db.cursor()
        self.preCursor = self.db.cursor(cursor_class=MySQLCursorPrepared,buffered=True)

    def insert(self,sql):
        try:
            self.cursor.execute(sql)
            print "Insertion Success"
            self.db.commit()

        except:
            self.db.rollback()
            print "Insertion Failure"

    def select_and_insert(self,sqls):
        self.cursor.execute(sqls)
        sqli = "insert into attendance (date, id, status) values (CURRENT_DATE,'%s','%s')"
        student = {}
        for (id,name) in self.cursor:
            student[id] = name
        for i in student:
            sqli = "insert into attendance (date, id, status) values (CURRENT_DATE,'%s','%s')"%(i,student[i])
            self.insert(sqli)


    def update(self,id,status):
        try:
            sql = "update attendance set status='%s' where id='%s' and date = CURRENT_DATE;"%(status,id)
            self.cursor.execute(sql)
            self.db.commit()
            print "attendance Success"
        except:
            self.db.rollback()
            print "attendance failure contact system admin"






