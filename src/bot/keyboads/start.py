from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_start_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Мои строки", callback_data="lines"),
    )
    builder.row(
        InlineKeyboardButton(text="Добавить строку", callback_data="add_line"),
        InlineKeyboardButton(
            text="Проверить баланс", callback_data="check_balance"
        ),
    )
    return builder.as_markup()
