import sqlite3

conn = sqlite3.connect('./person.db')

cursor = conn.cursor()

cursor.execute("SELECT * FROM PERSON_INFO")

rows = cursor.fetchall()

#print("num/name/age/sex")
for val in rows:
    print(val)

cursor.close()
conn.close()