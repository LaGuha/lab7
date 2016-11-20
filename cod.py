import MySQLdb

db=MySQLdb.connect(
	host='localhost',
	user='root',
	password='17021942',
	db='lab'
)

cur=db.cursor()

cur.execute('INSERT INTO table1 VALUES (id,"stroka")')

cur.commit()

cur.execute('SELECT * FROM table1;')

entries=cur.fetchall()

for e in entries:
	print (e)

cur.close()
db.close()