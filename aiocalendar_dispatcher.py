from aiogram import Dispatcher, Router, F

from handlers import select_date, change_month, change_year


class AiocalendarDispatcher:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.__instance = super(AiocalendarDispatcher, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.router = Router()

    async def setup(self, dispatcher: Dispatcher):
        """
        One-time DateCalendar setup.
            :param dispatcher: Dispatcher where you want to set up calendar
            :return:
        """
        self.router.callback_query(select_date, F.prefix=="date")
        self.router.callback_query(change_month, F.prefix=="select_month")
        self.router.callback_query(change_year, F.prefix=="select_year")
        dispatcher.include_router(self.router)







