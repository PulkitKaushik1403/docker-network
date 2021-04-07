host="localhost"
database="assignment"
user="passignment"
password="ppassword"
port="5434"

import psycopg2


con = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

print("Database opened successfully")
cur = con.cursor()
cur.execute("SELECT * from public.user")
rows = cur.fetchall()


for row in rows:
    print("FIRST NAME =", row[0])
    print("LAST NAME =", row[1])
    print("AGE =", row[2])
    print("PHONE =", row[3])
    print("ADDRESS =", row[4], "\n")

cur.close()
con.close()