import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from aiogram.utils import executor

from data.config import BOT_TOKEN
from data.repopsitory.groups_ import GroupRepository
from data.repopsitory.users_ import UserRepository
from domain.update import UpdateUsage

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dispatcher = Dispatcher(bot, storage=storage)


@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
    # check if type of chat group or supergroup
    if message.chat.type in [types.ChatType.GROUP, types.ChatType.SUPER_GROUP]:
        current_chat = await bot.get_chat(message.chat.id)
        # check chat is register
        if GroupRepository()._is_group_exist(current_chat['id']):
            await message.answer("Bot already started in this chat. Chat already get bitcoin update")
            return

        # try register chat
        if not GroupRepository()._add_group(current_chat['id'], current_chat['title'], current_chat['invite_link']):
            await message.answer("Was some exception when you have started bot. Try again later")
            return

        # successfully registered
        await message.answer("Chat has registered")
        return

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
    return


@dispatcher.message_handler(commands=['actually'])
async def actually(message: types.Message):
    # check if type of chat group or supergroup
    if message.chat.type in [types.ChatType.GROUP, types.ChatType.SUPER_GROUP]:
        current_chat = await bot.get_chat(message.chat.id)

        # check chat is register
        if not GroupRepository()._is_group_exist(current_chat['id']):
            await message.answer("Chat are not registered to get update. Input /start and register automatically")
            return

        response = UpdateUsage().access_update_actually(user_id=current_chat['id'])
        await message.answer(response)
        return

    # check user is register
    if not UserRepository()._is_user_exist(message.chat.id):
        await message.answer("You are not registered to get update. Input /start and register automatically")
        return

    response = UpdateUsage().access_update_actually(user_id=message.chat.id)
    await message.answer(response)
    return


if __name__ == '__main__':
    executor.start_polling(dispatcher=dispatcher, skip_updates=True)
