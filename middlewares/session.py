from aiogram import BaseMiddleware


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, session_pool):
        super().__init__()
        self.session_pool = session_pool

    async def __call__(self, handler, event, data):
        async with self.session_pool() as conn:
            data['session'] = conn
            return await handler(event, data)

