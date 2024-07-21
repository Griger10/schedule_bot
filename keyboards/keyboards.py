from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def build_command_keyboard(data_first, data_second_button):
    button_1 = InlineKeyboardButton(text='Числитель', callback_data=data_first)
    button_2 = InlineKeyboardButton(text='Знаменатель', callback_data=data_second_button)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_1, button_2]], resize_keyboard=True)
    return keyboard
