import psycopg2

conn = psycopg2.connect(database="testdb", user="tinastith-twine", host="127.0.0.1", port="5432")

print "Opened database successfully"

cur = conn.cursor()

cur.execute("""CREATE TABLE SENIOR_DAY_CENTERS(
	ID SERIAL PRIMARY KEY NOT NULL,
	NAME VARCHAR NOT NULL,
	ADDRESS CHAR,
	CITY TEXT,
	STATE TEXT,
	ZIPCODE TEXT
	);
 	""")



conn.commit()
conn.close()

