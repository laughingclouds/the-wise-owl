from sql import *
from time import strftime

mycursor = mydb.cursor()

def rdata(uid, content, time):   # short for register data
	'''
	This function will input 'content' into the mysql db (discord) table called 'user_input'
	'''
	global mycursor, mydb
	if IsOneInputFull(uid, mycursor):  # true if input already exists

		Update(mycursor, values=(str(content), str(time), int(uid)))  # update the value (see 'Update' definition)
	else:					 
		Insert(mycursor, values=(int(uid), str(content), str(time)))  # else insert value
	mydb.commit()  # make changes permanent


def qdata(uid, query='msg'):
    global mycursor
    command = f"SELECT {query} from user_input WHERE uid=%s"
    mycursor.execute(command, (uid,))
    msg = [msg for msg in mycursor][0][0]  # element inside a tuple which is inside a list
    if query == 'date':
        msg = int(msg.strftime("%Y%m%d%H%M%S"))
    return msg


def Delete(uid):
	global mycursor, mydb
	command = "DELETE FROM user_input WHERE uid=%s"
	mycursor.execute(command, (uid,))
	mydb.commit()