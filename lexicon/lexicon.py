from db.queries import get_groups
import asyncio

from sqlalchemy.ext.asyncio import async_sessionmaker

LEXICON_COMMANDS = {'/help': 'Справка по работе бота',
                    '/monday': 'Расписание на понедельник',
                    '/tuesday': 'Расписание на вторник',
                    '/wednesday': 'Расписание на среду',
                    '/thursday': 'Расписание на четверг',
                    '/friday': 'Расписание на пятницу',
                    '/set_group': 'Выбор расписания учебной группы'
                    }


LEXICON = {'start': f'Привет!\n\nЭтот бот позволяет получить расписание группы ИПсп-123 на '
                    f'определенный день недели с помощью простых команд\n\n'
                    f'Посмотреть команды вы можете в меню или воспользуйтесь командой /help',
           'help': f'Данный бот позволяет получить расписание на неделю\n\nВоспользуйтесь командой set_group '
                   f'с номером вашей группы из следующего списка:\n\n'
                   f'Пример использования: /set_group 1'}


ADMIN_LEXICON = {'admin': 'Админ-панель предлагает следующий функционал:\n\n/add_group - добавление группы в БД\n'
                          'Пример: /add_group ipsp123'}
