import sqlite3

conn = sqlite3.connect('./person.db')

cursor = conn.cursor()

cursor.execute("DELETE FROM PERSON_INFO WHERE AGE=29")

conn.commit() #commit을 해줘야 값이 반영됨

cursor.close()
conn.close()