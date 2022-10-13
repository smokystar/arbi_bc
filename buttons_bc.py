from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


a1 = KeyboardButton("Main menu")
a2 = KeyboardButton("Support")
key_menu_client = ReplyKeyboardMarkup(resize_keyboard=True)
key_menu_client.add(a1).add(a2)

b1 = KeyboardButton("activate")
tasks_menu = ReplyKeyboardMarkup(resize_keyboard=True)
tasks_menu.add(b1)