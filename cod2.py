import MySQLdb

class Connection:


	def __init__(self, user, password, db, host='localhost'):
		self.user=user
		self.password=password
		self.host=host
		self.db=db
		self._connection=None

	@property
	def connection(self):
		return self._connection

	def __enter__(self):
		self.connect()

	def __exit__(self, exc_type, exc_val, exc_tb ):
		self.disconnect()

	def connect(self):
		if not self._connection:
			self._connection=MySQLdb.connect(
				host=self.host,
				user=self.user,
				password=self.password,
				db=self.db
			)
	def disconnect(self):
		if self._connection:
			self._connection.close()

class Lane:

	def __init__(self,db_connection,lan):
		self.db_connection=db_connection.connection
		self.lan=lan

	def save(self):
		c=self.db_connection.cursor()
		c.execute('INSERT INTO table1(lane) VALUES (%s);',[(self.lan)])
		self.db_connection.commit()
		c.close()

con=Connection('root','17021942','lab')

with con:
	lane=Lane(con,'Toxas')
	lane.save()