from typing import Callable, Dict, Awaitable, Any

from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.types import CallbackQuery

from aiocalendar import DateCalendar


class CalendarMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        data['aiocalendar_handler'] = ...
        return await handler(event, data)
