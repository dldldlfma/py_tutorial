import sqlite3

conn = sqlite3.connect('./person.db')

cursor = conn.cursor()

cursor.execute("INSERT INTO PERSON_INFO(NUM,NAME,AGE,SEX) VALUES(1,'kuni',25,0)")
cursor.execute("INSERT INTO PERSON_INFO(NUM,NAME,AGE,SEX) VALUES(2,'suzy',29,1)")
cursor.execute("INSERT INTO PERSON_INFO(NUM,NAME,AGE,SEX) VALUES(3,'huni',29,0)")

conn.commit() #commit을 해줘야 값이 반영됨

cursor.close()
conn.close()