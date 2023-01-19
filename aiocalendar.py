import logging

from aiogram import Dispatcher, Bot, Router, F
from aiogram.fsm.state import State
from aiogram.fsm.storage.base import StorageKey
from aiogram.types import Message, InlineKeyboardMarkup

from functions import build_days_list, build_one_day_selector_kb
# from middlewares import CalendarMiddleware


class BaseAiocalendar:
    def __init__(self, bot: Bot, dispatcher: Dispatcher):
        self.handler = None
        self.dispatcher = dispatcher
        self.bot = bot
        self.storage_key = StorageKey(self.bot.id, 92, 92)
        # self.__router = Router()
        # self.__router.callback_query(CalendarMiddleware())
        # dispatcher.include_router(self.__router)

        logging.info("Aiocalendar created")


class DateCalendar(BaseAiocalendar):
    def __init__(self, bot, dispatcher):
        super().__init__(bot, dispatcher)

    async def __call__(self, function):
        """
        Decorator for date handler.
            :param function: function to decorate
        """

        async def wrapper(*args, **kwargs):
            return function(*args, **kwargs)

        return wrapper

    async def keyboard(self, chat_id, handler) -> InlineKeyboardMarkup:
        await self.dispatcher.storage.update_data(self.bot, self.storage_key, {str(chat_id):handler})
        return build_one_day_selector_kb(build_days_list())


