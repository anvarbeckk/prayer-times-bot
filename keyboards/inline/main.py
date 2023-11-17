from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="All Users 𖨆", callback_data="all_users"), InlineKeyboardButton(text="Ad", callback_data="advertising")],
    [InlineKeyboardButton(text="Clean Database (All users)", callback_data="clean_all_users")]
])
