import logging
from datetime import datetime, timedelta

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from aiogram.utils import executor

from data.config import BOT_TOKEN
from data.repopsitory.users_ import UserRepository
from domain.update import UpdateUsage

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dispatcher = Dispatcher(bot, storage=storage)


@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
    # check user is register
    if UserRepository()._is_user_exist(message.chat.id):
        await message.answer("Bot already started. You already get bitcoin update")
        return

    # try register user
    if not UserRepository()._add_user(message.chat.id, message.chat.username, message.chat.first_name, message.chat.last_name):
        await message.answer("Was some exception when you have started bot. Try again later")
        return

    # successfully registered
    await message.answer("You succesfully have started bot. You will get bitcoin update!")


@dispatcher.message_handler(commands=['actually'])
async def actually(message: types.Message):
    # check user is register
    if not UserRepository()._is_user_exist(message.chat.id):
        await message.answer("You are not registered to get update. Input /start and register automatically")
        return

    response = UpdateUsage().access_update_actually(user_id=message.chat.id)
    await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dispatcher, skip_updates=True)
