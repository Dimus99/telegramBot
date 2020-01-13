from config import *
import telebot
from functions import *
from keyboards import *
bot = telebot.TeleBot(TOKEN)
LizaUserName = '/////\\'

#bot body
WriteLog('good start')
@bot.message_handler(commands=['start'])
def HelloUser(message):
    SetNewUser(message.chat.id, message.chat.username, bot)
    sendToUser(bot, 'Приветствие от 711 комнаты', message.chat.id, startKeyboard)

#inline keyboard calls
@bot.callback_query_handler(func=lambda call: True)
def AnserForCall(call):
    WriteLog('call '+call.data+' @'+str(call.from_user.username))
    if call.data == 'нахуй':
        with open('besk-besk.jpg','rb') as img:
            sendImgToUser(bot, img, call.from_user.id)

    elif call.data == 'узнать':
        sendToUser(bot, 'в это беседе есть: '+' '.join(['@'+str(i[1]) for i in GetAllUsers()]), call.from_user.id)

    elif call.data == 'попросить':
        sendToUser(bot, 'Выбирай', call.from_user.id, askKeyboard)
    elif call.data[:3] == 'ask':
        sendingUsers = []
        if call.data[4:8]=='Лиза':
            global LizaUserName
            for user in GetAllUsers():
                if user[1]==LizaUserName:
                    sendToUser(bot, 'Лиза, пошли на свидание?', user[0])
                    WriteLog('отправлено для '+str(user[1])+' '+str(user[0]))
                    sendingUsers.append('@'+str(user[1]))
        else:
            for user in GetAllUsers():
                sendToUser(bot, call.data[4:], user[0])
                WriteLog('отправлено для '+str(user[1])+' '+str(user[0]))
                sendingUsers.append('@'+str(user[1]))

        sendToUser(bot,'End of sending, получатели: '+str(' '.join(sendingUsers)),call.from_user.id )

@bot.message_handler()
def HelloUser(message):
    if message.chat.id != 304228579:
        sendToUser(bot, message.text+' '+message.chat.username, 304228579)
        print('send to Dima '+ message.text)
    elif message.text[:4]=="SEND":
        for user in GetAllUsers():
                if user[1]==LizaUserName:
                    sendToUser(bot, message.text[4:]+' from @'+message.chat.username, user[0])
                    print('send to Liza '+ message.text[4:])


bot.polling()
