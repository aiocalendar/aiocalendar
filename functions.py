from calendar import Calendar
from datetime import datetime

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from utils import DateCallback, SelectYearCallback, SelectMonthCallback

calendar = Calendar()


def build_days_list(year=datetime.today().year, month=datetime.today().month)-> list[list[InlineKeyboardButton]]:
    calendar_dates = calendar.monthdayscalendar(year, month)
    kb_buttons = []

    for week in calendar_dates:
        row = [InlineKeyboardButton(text=str(day), callback_data=DateCallback(year=year, month=month, day=day).pack())
               if day else InlineKeyboardButton(text="ㅤ", callback_data="ㅤ")
               for day in week]
        kb_buttons.append(row)
    return kb_buttons


def build_one_day_selector_kb(days_buttons_list, year=datetime.today().year) -> InlineKeyboardMarkup:
    days_buttons_list = [[
        InlineKeyboardButton(text="<<", callback_data=SelectMonthCallback(month_op=1).pack()),
        InlineKeyboardButton(text=year, callback_data=SelectYearCallback(year=year).pack()),
        InlineKeyboardButton(text=">>", callback_data=SelectMonthCallback(month_op=1).pack())
    ]] + days_buttons_list
    return InlineKeyboardMarkup(
        inline_keyboard=days_buttons_list
    )
