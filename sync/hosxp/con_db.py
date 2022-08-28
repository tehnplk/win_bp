import pymysql.cursors

con = pymysql.connect(
    host='localhost',
    port=3306,
    user='sa',
    password='sa',
    database='log',
    cursorclass=pymysql.cursors.DictCursor
)
