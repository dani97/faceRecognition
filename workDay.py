from DBAccess import DBAccess

db = DBAccess()
sql = "select * from student"
db.select_and_insert(sql)


