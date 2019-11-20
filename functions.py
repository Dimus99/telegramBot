
def sendToUser(bot, message, id_user, keyboard=None):
    try:
        bot.send_message(id_user, message, reply_markup=keyboard)
    except:
        WriteLog(f'error with send message to {id_user}')

def WriteLog(messLog, bot=None):
    DimaId=304228579
    if bot!=None:
        sendToUser(bot, 'Console: '+messLog, DimaId)

    print(messLog)

def sendImgToUser(bot, img, id_user):
    try:
        bot.send_photo(id_user, img)
    except:
        WriteLog(f'error with send message to {id_user}')

def SetNewUser(userId, username, bot):
    userId=str(userId)
    import sqlite3 as sq
    conn = sq.connect('database.db')
    cursor = conn.cursor()
    sql = f"""
	SELECT *
	FROM users
	WHERE id = '{userId}'
	"""
    cursor.execute(sql)
    if cursor.fetchone()==None:
	    #новый пользователь
    	sql=f"""INSERT INTO users
    	VALUES ('{userId}','{username}','0')"""
    	cursor.execute(sql)
    	WriteLog('новый пользователь в БД, '+str(username),bot)
    else:
        WriteLog('Приветсвтуем @'+username,bot )
    conn.commit()

def GetAllUsers():
	import sqlite3 as sq
	conn = sq.connect('database.db')
	cursor = conn.cursor()
	sql = """
	SELECT *
	FROM users
	"""
	cursor.execute(sql)

	res=[]
	for user in cursor.fetchall():
		res.append([user[0],user[1],user[2]])
	conn.commit()
	return res

WriteLog('good import functions')