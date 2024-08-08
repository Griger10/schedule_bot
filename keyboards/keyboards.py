from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def build_command_keyboard(numerator, denominator, data_first, data_second):
    button_1 = InlineKeyboardButton(text=numerator, callback_data=data_first)
    button_2 = InlineKeyboardButton(text=denominator, callback_data=data_second)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_1, button_2]], resize_keyboard=True)
    return keyboard
