from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


async def start_command_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn.add(
        KeyboardButton(text="Sherik kerak"),
        KeyboardButton(text="Ish joyi kerak"),
        KeyboardButton(text="Hodim kerak"),
        KeyboardButton(text="Ustoz kerak"),
        KeyboardButton(text="Shogird kerak"),
    )

    return btn


async def yesno_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn.add(
        KeyboardButton(text="HA"),
        KeyboardButton(text="YO'Q")
    )

    return btn


async def admin_btn():
    btn = InlineKeyboardMarkup(row_width=1)

    btn.add(
        InlineKeyboardButton(text="Tasdiqlash", callback_data="yes"),
        InlineKeyboardButton(text="Bekor qilish", callback_data="no")
    )
    return btn
