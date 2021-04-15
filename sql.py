import mysql.connector


mydb = mysql.connector.connect(
	host='localhost',
	user='root',
	password='alphabet',
	database='discord'
	)


def CheckIfTableExists():  # for later for error handling
	'''This function should check if the table where
	the data is supposed to be entered exists.
	'''


def IsOneInputFull(uid, cursor):  # read db to make sure there's only one input per user
	command = "SELECT msg FROM user_input WHERE uid=%s"
	cursor.execute(command, (uid,))
	temp_list = [_ for _ in cursor]
	if temp_list:
		return True
	else:
		return False


def Update(cursor, values:tuple):   # update data in table
	# note the order at which the values are to be entered
	command = "UPDATE user_input SET msg=%s, date=%s WHERE uid=%s"
	cursor.execute(command, values)  # 'value' is a tuple


def Insert(cursor, values:tuple):   # insert data into table
	command = "INSERT INTO user_input VALUES (%s, %s, %s)"
	cursor.execute(command, values)
