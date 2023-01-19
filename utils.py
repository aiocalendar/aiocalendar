from aiogram.filters.callback_data import CallbackData


class DateCallback(CallbackData, prefix="date"):
    year: int
    month: int
    day: int


class SelectYearCallback(CallbackData, prefix="select_year"):
    year: int


class SelectMonthCallback(CallbackData, prefix="select_month"):
    month_op: int
