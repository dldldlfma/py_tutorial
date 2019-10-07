import sqlite3

conn = sqlite3.connect('./person.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE PERSON_INFO(NUM INT(16), NAME CHAR(32), AGE INT(8), SEX INT(1))")

cursor.close()
conn.close()
