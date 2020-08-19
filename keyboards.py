from telebot import types
from functions import *
startKeyboard = types.InlineKeyboardMarkup()
startKeyboard.add(types.InlineKeyboardButton( 'Попросить о чем-то', callback_data='попросить' ))
startKeyboard.add(types.InlineKeyboardButton( 'Узнать кто тут есть', callback_data='узнать' ))
startKeyboard.add(types.InlineKeyboardButton( 'Бесконечность', callback_data='бесконечность'))

askKeyboard = types.InlineKeyboardMarkup()
askKeyboard.add(types.InlineKeyboardButton( 'Разолслать всем, что день прошел необычно', callback_data='ask_День' ))
askKeyboard.add(types.InlineKeyboardButton( 'Попросить Всех собраться в 711', callback_data='ask_Время сбора , пригоняй)' ))
askKeyboard.add(types.InlineKeyboardButton( 'Поставить свечку за Глеба', callback_data='ask_ГЕГ инсайд'))
askKeyboard.add(types.InlineKeyboardButton( 'Позвать Лизу на свидание', callback_data='ask_Лиза, пошли на свидание?'))

WriteLog('good import keyboards')
