import psycopg2

conn = psycopg2.connect(database="testdb", user="tinastith-twine", host="127.0.0.1", port="5432")

print "Opened database successfully"

cur = conn.cursor()

# How to create a table

# cur.execute("""CREATE TABLE MEMORY(
#  	ID INT PRIMARY KEY NOT NULL,
#  	NAME VARCHAR NOT NULL,
#  	DEFINITION INT NOT NULL,
#  	DIAGNOSIS CHAR(50),
#  	TYPES TEXT ,
#  	TREATMENTS  TEXT ,
#  	CAUSES TEXT ,
#  	SYMPTONS TEXT , 
#  	MEDICATIONS TEXT
#  	); 
# 	""")
 		

# cur.execute(""" INSERT INTO MEMORY (ID, NAME, DEFINITION)
# 	 (ID, "Alzheimers Disease", "Alzheimers disease is an irreversible");
# 	  """)

# Work on API-  & POSTGRES- 11/21/16.
# Go to APLACEforMom they all the API's for Memory Care

cur.execute("""CREATE TABLE MEMORY_CARE_FACILITIES(
			ID SERIAL PRIMARY KEY NOT NULL,
			NAME VARCHAR NOT NULL,
			ADDRESS CHAR,
			CONTACT VARCHAR,
			SERVICE_PROVIDED VARCHAR,
			LINK VARCHAR
			);
			""")


			
 


#cur.execute("DELETE from COMPANY where ID = 2;")

conn.commit()

#print "Total number of rows deleted :", cur.rowcount 

# cur.execute("SELECT id, name, address, salary from COMPANY")
# rows = cur.fetchall()
# for row in rows:
# 	print "ID = ", row[0]
# 	print "NAME = ", row[1]
# 	print "ADDRESS = ", row[2]
# 	print "SALARY = ", row[3], "/n"
# 	
# print "Operation done successfully";



conn.close()