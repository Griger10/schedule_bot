import logging

from aiogram import BaseMiddleware

logger = logging.getLogger(__name__)


class TranslatorRunnerMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        user = data.get('event_from_user')

        if user is None:
            return await handler(event, data)

        hub = data.get('_translator_hub')
        data['i18n'] = hub.get_translator_by_locale(locale='ru')

        return await handler(event, data)

