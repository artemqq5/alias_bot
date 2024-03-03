import logging
import random

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode, ReplyKeyboardRemove
from aiogram.utils import executor

from data.config import BOT_TOKEN
from data.repopsitory.chats_ import ChatRepository
from quetions import LIST_OF_QUESTION

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dispatcher = Dispatcher(bot, storage=storage)


@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type in [types.ChatType.GROUP, types.ChatType.SUPER_GROUP]:

        invite_link = await bot.get_chat(message.chat.id)

        if ChatRepository().add_chat(message.chat.id, message.chat.title, invite_link['invite_link']):
            await message.answer("Група була додана успішно")
        else:
            await message.answer("Виникла помилка. Можливо група вже додана")

    elif message.chat.type in [types.ChatType.PRIVATE, ]:
        await message.answer(
            "<b>Привіт, це бот для гри в Alias</b>\n\n"
            "Додайте до групи цього бота як адміна та введіть команду /start\n\n"
            "Потім для генерації питань вводьте команду /question",
            reply_markup=ReplyKeyboardRemove()
        )


@dispatcher.message_handler(commands=['question'])
async def question(message: types.Message):
    if message.chat.type in [types.ChatType.GROUP, types.ChatType.SUPER_GROUP]:
        if ChatRepository().is_exists(message.chat.id):
            await message.answer(random.choice(LIST_OF_QUESTION))
        else:
            await message.answer("Група ще не додана, напишіть /start")


if __name__ == '__main__':
    executor.start_polling(dispatcher=dispatcher, skip_updates=True)
