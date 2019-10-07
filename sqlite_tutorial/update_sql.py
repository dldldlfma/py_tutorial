import sqlite3

conn = sqlite3.connect('./person.db')

cursor = conn.cursor()

cursor.execute("UPDATE PERSON_INFO SET AGE=29 WHERE NAME='kuni' ")

conn.commit() #commit을 해줘야 값이 반영됨

cursor.close()
conn.close()